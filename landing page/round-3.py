import re
import os
import time
import requests
import hashlib
from model import Round_3_New
from timestamp import datetime_timestamp, timestamp_datetime, get_now_timestamp
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy.sql import and_, asc, desc, or_
from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker

screenshots_save_path = './data/round-2/'  # 第三轮和第二轮存一起吧，无所谓
sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
proxy = '127.0.0.1:1080'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
}


def visit(url_in_comment, landing_page_1, landing_page_2, browser, session):
    try:
        print("visiting: ", landing_page_2)
        cur_domain = landing_page_2.split('/')[2]
        links = []
        browser.get(landing_page_2)
        # 提取所有a标签
        try:
            a_tags = browser.find_elements_by_tag_name('a')
        except:
            return
        for a_tag in a_tags:
            try:
                link = a_tag.get_attribute('href')
                if 'http' in link:
                    links.append(link)
            except:
                continue
        links = list(set(links))
        for link in links:
            print('link: ', link)
            browser.get(link)
            print("* ", browser.current_url)
            domain = browser.current_url.split('/')[2]
            if domain != cur_domain:
                round_3_new = Round_3_New()
                round_3_new.url = url_in_comment
                round_3_new.landing_page_1 = landing_page_1
                round_3_new.landing_page_2 = landing_page_2
                round_3_new.landing_page_3 = browser.current_url
                round_3_new.landing_page_md5 = hashlib.md5(round_3_new.landing_page_3.encode('UTF-8')).hexdigest()
                round_3_new.checked = ''
                try:
                    save_name = screenshots_save_path + round_3_new.landing_page_md5 + '.png'
                    if not os.path.exists(save_name):
                        browser.save_screenshot(save_name)
                        print("截图成功")
                    else:
                        print("截图已存在")
                except BaseException as err_msg:
                    print("截图失败：%s" % err_msg)
                round_3_new.create_time = get_now_timestamp()
                session.add(round_3_new)
                session.commit()
    except Exception as e:
        print("* Error: ", e)


if __name__ == '__main__':
    # # 正常模式
    # browser = webdriver.Chrome()
    # browser.maximize_window()
    # headless模式
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument("--window-size=1920,1080")
    option.add_argument("--mute-audio")  # 静音
    browser = webdriver.Chrome(chrome_options=option)
    browser.implicitly_wait(20)
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try:
        with open("url_round_3.txt", "r", encoding="UTF8") as f:
            items = f.readlines()
        for item in items:
            item = item.strip()
            print('----------')
            url_in_comment = item.split('\t')[0]
            landing_page_1 = item.split('\t')[1]
            landing_page_2 = item.split('\t')[2]
            rows = session.query(Round_3_New).filter(Round_3_New.url.like(url_in_comment),
                                                     and_(Round_3_New.landing_page_1.like(landing_page_1)),
                                                     and_(Round_3_New.landing_page_2.like(landing_page_2))).all()
            if rows:
                print("*** Already Visited. ***")
                continue
            visit(url_in_comment, landing_page_1, landing_page_2, browser, session)
            # break  # for test
    except Exception as e:
        print("Error: ", e)
    finally:
        browser.close()
        browser.quit()
        session.close()
