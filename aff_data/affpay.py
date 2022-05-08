import os
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
from model import Affpay_Offer
from bs4 import BeautifulSoup

sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
url_prefix = 'https://www.affplus.com/search?verticals=Adult&page='  # 后面加页数
# url_prefix = 'https://www.affplus.com/search?verticals=Dating&page='  # 后面加页数
PAGE_COUNT = 200
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
            ele = browser.find_element_by_class_name(element)
        elif condition == 'id':
            ele = browser.find_element_by_id(element)
        elif condition == 'xpath':
            ele = browser.find_element_by_xpath(element)
        return ele
    except Exception as err:
        return False


def get_offer(offer_link, browser, engine):
    print("--------------------------------")
    print("Visiting Offer: ", offer_link)
    js = 'window.open(\"' + offer_link + '\");'
    browser.execute_script(js)
    time.sleep(2)
    handles = browser.window_handles
    browser.switch_to.window(handles[1])  # 切换标签页
    affpay_offer = Affpay_Offer()
    affpay_offer.url = offer_link
    try:
        affpay_offer.title = browser.find_element_by_css_selector('h1.richtext').text
        # print("title: ", affpay_offer.title)
        affpay_offer.status = browser.find_element_by_css_selector('span.bg-green-500').text
        # print("status了", affpay_offer.status)
        affpay_offer.offer_create_time = browser.find_element_by_xpath(
            '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/div/span[2]').text
        # print("create: ", affpay_offer.offer_create_time)
        affpay_offer.offer_update_time = browser.find_element_by_xpath(
            '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/div/span[3]').text
        # print("update: ", affpay_offer.offer_update_time)
        affpay_offer.create_time = get_now_timestamp()
        affpay_offer.payout = browser.find_element_by_xpath(
            '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/span[1]').text + '/' + browser.find_element_by_xpath(
            '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/span[2]').text
        # print("payout: ", affpay_offer.payout)
        affpay_offer.network = browser.find_element_by_xpath(
            '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/h3').text
        # print("network: ", affpay_offer.network)
    except Exception as err:
        print("Error: ", err)

    affpay_offer.geo = ''
    geos = browser.find_element_by_xpath(
        '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[3]')
    geos = geos.find_elements_by_tag_name('span')
    for geo in geos:
        affpay_offer.geo = affpay_offer.geo + ' ' + geo.text

    # affpay的offer有category为空的情况，但是我们已经选择category了，所以不考虑判断元素是否存在了
    affpay_offer.category = browser.find_element_by_xpath(
        '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/span[2]').text

    affpay_offer.land_page_img = ''
    try:
        img_src = browser.find_element_by_xpath(
            '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/img').get_attribute(
            'src')
        img_src = img_src.replace("https", "http")
        img_path = './data/affpay/' + img_src.split('/')[-1]
        affpay_offer.land_page_img = img_src.split('/')[-1]
        if not os.path.exists(img_path):
            print("Getting Img {0}...".format(img_src))
            r = requests.get(img_src, headers=headers, timeout=8, verify=False, proxies=proxies)
            with open(img_path, "wb") as f:
                f.write(r.content)
                print("Img Successfully Gotten.")
        else:
            print("Img Already Exists.")
    except Exception as err:
        print("Getting Preview Img Error: ", err)

    affpay_offer.land_page = ''
    try:
        browser.find_element_by_xpath(
            '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]').click()
        time.sleep(3)
        handles = browser.window_handles
        browser.switch_to.window(handles[2])
        affpay_offer.land_page = browser.current_url

        # 网站截图比预览图更清楚一点
        try:
            screenshot = '.\\data\\affpay\\screenshots\\' + affpay_offer.land_page_img.replace(".jpg", "") + '.png'
            if not os.path.exists(screenshot):
                browser.save_screenshot(screenshot)
                print("Take Screenshot successfully.")
            else:
                print("Screenshot Already Exists.")

        except BaseException as err_msg:
            print("截图失败：%s" % err_msg)

        browser.close()
        browser.switch_to.window(handles[1])
        time.sleep(0.5)
    except Exception as err:
        print("Getting Preview Landing Page Error: ", err)

    # description 麻烦死了
    affpay_offer.description = ''
    try:
        show_more_btn = browser.find_element_by_xpath(
            '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div/span')
        show_more_btn.click()
    except Exception as err:
        print("No Show More Btn.")
        # print("Error Detail: ", err)
    try:
        # 情况太多，直接处理html算了
        description = browser.find_element_by_xpath(
            '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[3]/div').get_attribute(
            'innerHTML')
        soup = BeautifulSoup(description, "lxml")
        description = soup.get_text()
        affpay_offer.description = description
    except Exception as err:
        print("Getting Description Error: ", err)

    # for test
    print("offer title: ", affpay_offer.title)
    print("offer status: ", affpay_offer.status)
    print("offer create time: ", affpay_offer.offer_create_time)
    print("offer update time: ", affpay_offer.offer_update_time)
    print("offer description: ", affpay_offer.description)
    print("offer land page: ", affpay_offer.land_page)
    print("offer land page img: ", affpay_offer.land_page_img)
    print("offer category: ", affpay_offer.category)
    print("offer geo: ", affpay_offer.geo)
    print("offer network: ", affpay_offer.network)
    print("offer payout: ", affpay_offer.payout)
    print("time: ", affpay_offer.create_time)

    session.add(affpay_offer)
    session.commit()


if __name__ == '__main__':
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

    for i in range(1, PAGE_COUNT + 1):
        try:
            print("--------------------")
            print("Getting Page {0}...".format(i))
            url = url_prefix + str(i)
            browser.get(url)
            time.sleep(2)
            main_handle = browser.current_window_handle
            offer_links = browser.find_elements_by_css_selector('h2.mb-1 a')
            for offer_link in offer_links:
                link = offer_link.get_attribute('href')
                get_offer(link, browser, engine)
                browser.close()
                browser.switch_to.window(main_handle)
                time.sleep(0.5)
                break  # for test
            break  # for test
        except Exception as err:
            print("Error: ", err)
    browser.quit()
