import os
import re
import time
import lxml
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy.sql import and_, asc, desc, or_
from timestamp import get_now_timestamp
from model import Odigger_Offer
from bs4 import BeautifulSoup

sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
url_prefix = 'https://odigger.com/offers?search=adult&page='
PAGE_COUNT = 250
MAX_REFRESH_TIME = 20
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
proxy = '127.0.0.1:1080'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
}


def check_if_exist(browser, element, condition):
    try:
        if condition == 'class':
            browser.find_element_by_class_name(element)
        elif condition == 'id':
            browser.find_element_by_id(element)
        elif condition == 'xpath':
            browser.find_element_by_xpath(element)
        elif condition == 'css':
            browser.find_element_by_css_selector(element)
        return True
    except Exception as err:
        return False


def get_offer(browser, offer_link, session):
    js = 'window.open(\"' + offer_link + '\");'
    browser.execute_script(js)
    time.sleep(3)
    handles = browser.window_handles
    browser.switch_to.window(handles[1])  # 切换标签页

    odigger_offer = Odigger_Offer()
    odigger_offer.title = ''
    odigger_offer.url = offer_link
    odigger_offer.category = ''
    odigger_offer.land_page_img = ''
    odigger_offer.land_page = ''
    odigger_offer.geo = ''
    odigger_offer.offer_update_time = ''
    odigger_offer.offer_create_time = ''
    odigger_offer.network = ''
    odigger_offer.payout = ''
    odigger_offer.description = ''
    odigger_offer.status = ''

    try:
        tbody = browser.find_element_by_xpath(
            '//*[@id="app"]/section/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div/table/tbody')
        trs = tbody.find_elements_by_tag_name('tr')
        for tr in trs:
            td_1 = tr.find_elements_by_tag_name('td')[0]
            td_2 = tr.find_elements_by_tag_name('td')[1]
            if td_1.text == 'Offer Name:':
                odigger_offer.title = td_2.text
            elif td_1.text == 'Preview:':
                odigger_offer.land_page = td_2.find_element_by_tag_name('a').get_attribute('href')
            elif td_1.text == 'Categories:':
                odigger_offer.category = td_2.text
            elif td_1.text == 'Network:':
                odigger_offer.network = td_2.text
            elif td_1.text == 'Status:':
                odigger_offer.status = td_2.text
            elif td_1.text == 'Last Updated:':
                odigger_offer.offer_update_time = td_2.text
            elif td_1.text == 'Date Added:':
                odigger_offer.offer_create_time = td_2.text
            elif td_1.text == 'Payouts:':
                odigger_offer.payout = td_2.text
            elif td_1.text == 'Countries:':
                try:
                    # 要展开的
                    geo_list = []
                    td_2.find_element_by_css_selector('span > a').click()
                    country_popovr = td_2.find_element_by_css_selector('div.country-popovr')
                    geos = country_popovr.find_elements_by_tag_name('a')
                    for geo in geos:
                        geo_list.append(geo.text)
                    if 'X' in geo_list:
                        geo_list.remove('X')
                    odigger_offer.geo = ' '.join(geo_list)
                except:
                    # 不需要展开的
                    odigger_offer.geo = td_2.find_element_by_css_selector('span').text
    except Exception as err:
        print("** Get Basic Info Err. **")
        print(err)

    try:
        odigger_offer.description = browser.find_element_by_xpath(
            '//*[@id="app"]/section/div/div/div[2]/div/div[1]/div[4]/div[1]/div/div/div').text
    except Exception as err:
        print("** Get Description Error **")
        print(err)

    # Preview Landing Page Img
    try:
        img_src = browser.find_element_by_xpath(
            '//*[@id="app"]/section/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/ul/li[1]/img').get_attribute(
            'src')
        img_src = img_src.replace("https", "http")
        img_path = './data/odigger/' + img_src.split('/')[-2] + '.jpg'
        odigger_offer.land_page_img = img_src.split('/')[-2] + '.jpg'
        if not os.path.exists(img_path):
            print("--Getting Img {0} --".format(img_src))
            r = requests.get(img_src, headers=headers, timeout=8, proxies=proxies)
            with open(img_path, "wb") as f:
                f.write(r.content)
                print("--Successfully Got Img.--")
        else:
            print("--Img Already Exists.--")

    except Exception as err:
        print("** Getting Preview Img Error **")
        print(err)

    # Landing Page
    if odigger_offer.land_page:
        try:
            js = 'window.open(\"' + odigger_offer.land_page + '\");'
            browser.execute_script(js)
            time.sleep(1)
            handles = browser.window_handles
            browser.switch_to.window(handles[2])  # 切换标签页
            time.sleep(2)
            if browser.title:
                # 截图
                try:
                    screenshot = '.\\data\\odigger\\screenshots\\' + odigger_offer.land_page_img.replace(".jpg",
                                                                                                         "") + '.png'
                    if not os.path.exists(screenshot):
                        browser.save_screenshot(screenshot)
                        print("--Take Screenshot successfully.--")
                    else:
                        print("--Screenshot Already Exists.--")

                except Exception as err:
                    print("** Failed To Take Screenshots. **")
                    print(err)

            browser.close()
            browser.switch_to.window(handles[1])
            time.sleep(1)
        except Exception as err:
            print("Get Landing Page Error.")
            print(err)

    print("offer title: ", odigger_offer.title)
    print("offer landing page: ", odigger_offer.land_page)
    print("offer category: ", odigger_offer.category)
    print("offer network: ", odigger_offer.network)
    print("offer status: ", odigger_offer.status)
    print("offer update time: ", odigger_offer.offer_update_time)
    print("offer create time: ", odigger_offer.offer_create_time)
    print("offer payout: ", odigger_offer.payout)
    print("offer geo: ", odigger_offer.geo)
    print("offer description: ", odigger_offer.description)
    print("offer landing page img: ", odigger_offer.land_page_img)

    odigger_offer.create_time = get_now_timestamp()

    session.add(odigger_offer)
    session.commit()


if __name__ == '__main__':
    start_page = int(input('Start Page: '))
    end_page = int(input('End Page: '))
    # 正常模式
    browser = webdriver.Chrome()
    browser.maximize_window()
    # headless模式
    # option = webdriver.ChromeOptions()
    # option.add_argument('--headless')
    # option.add_argument("--window-size=1920,1080")
    # browser = webdriver.Chrome(chrome_options=option)
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    try:
        for page in range(start_page, end_page + 1):
            print("---Current Page: {0}---".format(page))
            url = url_prefix + str(page)
            browser.get(url)
            time.sleep(4)
            # 这网站太拉了 加载不出来就刷新
            refresh_time = MAX_REFRESH_TIME
            while refresh_time:
                if check_if_exist(browser, '#search-page-offers-table > tbody > tr', 'css'):
                    print("Loading Successfully.")
                    break
                browser.refresh()
                time.sleep(4)
                refresh_time = refresh_time - 1
            trs = browser.find_elements_by_css_selector('#search-page-offers-table > tbody > tr')
            main_handle = browser.current_window_handle
            for tr in trs:
                offer_link = tr.find_element_by_css_selector('h6 > a').get_attribute('href')
                rows = session.query(Odigger_Offer).filter(Odigger_Offer.url.like(offer_link)).all()
                if rows:
                    print("---Offer {0} Has Already Been Visited---".format(offer_link))
                    continue

                print("--- Getting Offer {0} ---".format(offer_link))
                get_offer(browser, offer_link, session)
                print("--- Successfully Got ---")
                browser.close()
                browser.switch_to.window(main_handle)
                time.sleep(1)
                print("Reminder: Page{0} - {1}".format(start_page, end_page))
                # break # for test


    except Exception as err:
        print(err)

    browser.quit()
    session.close()
