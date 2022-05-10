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
from model import Offervault_Offer
from bs4 import BeautifulSoup

sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
url = 'https://offervault.com/?selectedTab=topOffers&search=&page=1'
PAGE_COUNT = 250
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
        return True
    except Exception as err:
        return False


def get_offer(browser, session, offer_link):
    print("---Visiting Offer: {0}...".format(offer_link))
    js = 'window.open(\"' + offer_link + '\");'
    browser.execute_script(js)
    time.sleep(2)
    handles = browser.window_handles
    browser.switch_to.window(handles[1])  # 切换标签页

    offervault_offer = Offervault_Offer()
    offervault_offer.url = offer_link
    offervault_offer.title = ''
    offervault_offer.payout = ''
    offervault_offer.category = ''
    offervault_offer.network = ''
    offervault_offer.offer_update_time = ''
    offervault_offer.geo = ''
    offervault_offer.description = ''
    offervault_offer.land_page_img = ''
    offervault_offer.land_page = ''

    preview_url = ''

    # 本来就没有
    offervault_offer.offer_create_time = ''
    try:
        tbody = browser.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/table/tbody')
        # 防止像affpay一样有的项没有
        items = tbody.find_elements_by_tag_name('tr')
        for item in items:
            th = item.find_element_by_tag_name('th').text
            td = item.find_element_by_tag_name('td')
            if th == 'Offer Name:':
                offervault_offer.title = td.text
            elif th == 'Payout:':
                offervault_offer.payout = td.text
            elif th == 'Categories:':
                offervault_offer.category = td.text
            elif th == 'Network:':
                offervault_offer.network = td.text
            elif th == 'Last Updated:':
                offervault_offer.offer_update_time = td.text
            elif th == 'Countries:':
                # 麻烦死了
                try:
                    # 要展开的
                    a = td.find_element_by_tag_name('a').click()
                    # ul = browser.find_element_by_xpath('//*[@id="__bv_popover_116__"]/div[2]/div/ul')
                    # 太狗了 id 是动态变化的 要自己写xpath
                    ul = browser.find_element_by_css_selector(
                        'div.popover > div.popover-body > div.country-popovr > ul')
                    countries = ul.find_elements_by_tag_name('a')
                    geos = []
                    for country in countries:
                        # print("country: ", country.text)
                        geos.append(country.text)
                    offervault_offer.geo = ' '.join(geos)
                except Exception as err:
                    # 不用展开的
                    spans = td.find_elements_by_tag_name('span')
                    geos = []
                    for span in spans:
                        if span.text:
                            # print("span: ", span.text)
                            geos.append(span.text)
                    geos = list(set(geos))  # 不知道为什么会有重复的不想找原因了反正就这样去个重算了
                    offervault_offer.geo = ' '.join(geos)
            elif th == 'Preview:':
                try:
                    preview_url = td.find_element_by_tag_name('a').get_attribute('href')
                except Exception as err:
                    print("No Preview Available.")
                    print(err)

    except Exception as err:
        print(err)

    try:
        offervault_offer.description = browser.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/div/div/div/div/div[1]/div[1]/div[2]/div[3]/div').text
    except Exception as err:
        print("No Description.")
        print(err)

    # Img
    try:
        img_src = browser.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/div/div/div/div/div[1]/div[1]/div[2]/div[2]/div/a/img').get_attribute(
            'src')
        img_src = img_src.replace("https", "http")
        img_path = './data/offervault/' + img_src.split('/')[-2] + '.jpg'
        offervault_offer.land_page_img = img_src.split('/')[-2] + '.jpg'
        if not os.path.exists(img_path):
            print("Getting Img {0}...".format(img_src))
            r = requests.get(img_src, headers=headers, timeout=8, proxies=proxies)
            with open(img_path, "wb") as f:
                f.write(r.content)
                print("Img Successfully Gotten.")
        else:
            print("Img Already Exists.")

    except Exception as err:
        print("Getting Preview Img Error")
        print(err)

    # Landing Page
    if preview_url:
        try:
            js = 'window.open(\"' + preview_url + '\");'
            browser.execute_script(js)
            time.sleep(2.5)
            handles = browser.window_handles
            browser.switch_to.window(handles[2])  # 切换标签页

            offervault_offer.land_page = browser.current_url
            # 截图
            try:
                screenshot = '.\\data\\offervault\\screenshots\\' + offervault_offer.land_page_img.replace(".jpg",
                                                                                                           "") + '.png'
                if not os.path.exists(screenshot):
                    browser.save_screenshot(screenshot)
                    print("Take Screenshot successfully.")
                else:
                    print("Screenshot Already Exists.")

            except Exception as err:
                print("Failed To Take Screenshots.")
                print(err)

            browser.close()
            browser.switch_to.window(handles[1])
            time.sleep(0.5)
        except Exception as err:
            print("Get Landing Page Error.")
            print(err)

    offervault_offer.create_time = get_now_timestamp()

    # for test
    print("offer title: ", offervault_offer.title)
    print("offer payout: ", offervault_offer.payout)
    print("offer geo: ", offervault_offer.geo)
    print("offer network: ", offervault_offer.network)
    print("offer update time: ", offervault_offer.offer_update_time)
    print("offer category: ", offervault_offer.category)
    print("offer landing page: ", offervault_offer.land_page)

    session.add(offervault_offer)
    session.commit()


def get_next_page(browser, retry):
    try:  # 可能出错 stale element reference: element is not attached to the page document
        if retry == 10:
            return
        next_page = browser.find_element_by_xpath(
            '//*[@id="__layout"]/div/section[2]/div/div/div/div[1]/div[1]/div/div/div[2]/ul/li[10]/button')
        next_page.click()
        time.sleep(2)
        retry = 0
        return
    except:
        retry = retry + 1
        get_next_page(browser, retry)


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

    try:
        # 选择adult分类
        browser.get(url)  # 离谱的是不挂代理就会进We are checking your browser界面并卡在这个界面
        browser.implicitly_wait(3)
        multi_select = browser.find_element_by_xpath(
            '//*[@id="__layout"]/div/section[1]/div[1]/div/div[1]/div[1]/div/div[1]/ul/li[3]/div/div[1]')
        ActionChains(browser).move_to_element(multi_select).click().perform()  # **必须要模拟鼠标悬浮否则没反应
        adult_tag = browser.find_element_by_xpath(
            '//*[@id="__layout"]/div/section[1]/div[1]/div/div[1]/div[1]/div/div[1]/ul/li[3]/div/div[3]/ul/li[3]')
        ActionChains(browser).move_to_element(adult_tag).click().perform()
        time.sleep(3)

        while True:
            main_handle = browser.current_window_handle
            url = browser.current_url
            page = re.findall(r'page=[0-9]+', url)[0][5:]
            print("-------Current Page: {0}-------".format(page))
            # 获取当前页offer链接
            container = browser.find_element_by_css_selector('#index-page-offerstable > tbody')
            links = container.find_elements_by_tag_name('a')
            for link in links:
                offer_link = link.get_attribute('href')
                # 过滤 javascript:;
                if offer_link == 'javascript:;':
                    continue
                # 检查是否已经爬取过这个offer了
                rows = session.query(Offervault_Offer).filter(Offervault_Offer.url.like(offer_link)).all()
                if rows:
                    print("*** Offer {0} Has Already Been Visited. ***".format(offer_link))
                    continue
                # # 折叠countries测试
                # offer_link = 'https://offervault.com/offer/b2cdfbacede6f41df8017045d803b1df/badoink-vod-nz-au-ca-gb-us'
                get_offer(browser, session, offer_link)
                browser.close()
                browser.switch_to.window(main_handle)
                time.sleep(0.5)
            #     break  # for test
            # break  # for test

            # 判断是否还有下一页
            if not check_if_exist(browser,
                                  '//*[@id="__layout"]/div/section[2]/div/div/div/div[1]/div[1]/div/div/div[2]/ul/li[10]/button',
                                  'xpath'):
                break
            else:
                # 跳转到下一页
                get_next_page(browser, 0)


    except Exception as err:
        print(err)

    browser.quit()
    session.close()
