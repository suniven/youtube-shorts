import re
import os
import time
import requests
import hashlib
from model import Round_2
from timestamp import datetime_timestamp, timestamp_datetime, get_now_timestamp
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy.sql import and_, asc, desc, or_
from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker

screenshots_save_path = './data/round-2/'
sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
proxy = '127.0.0.1:1080'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
}


def visit(url, browser, session):
    try:
        print("visiting: ", url)
        cur_domain = url.split('/')[2]
        links = []
        browser.get(url)
        # 判断iframe
        try:
            iframes = browser.find_elements_by_tag_name('iframe')
            if len(iframes) != 0:
                with open('url_round_1_iframe.txt', 'a') as f:
                    f.write(url + '\n')
        except:
            print("No iframe.")

        # 提取所有a标签
        a_tags = browser.find_elements_by_tag_name('a')
        for a_tag in a_tags:
            link = a_tag.get_attribute('href')
            links.append(link)
        links = list(set(links))
        for link in links:
            if 'http' not in link:
                with open('url_round_1_js.txt', 'a') as f:
                    f.write(url + '\n')
                continue
            print('link: ', link)
            browser.get(link)
            print("* ", browser.current_url)
            domain = browser.current_url.split('/')[2]
            if domain != cur_domain:
                round_2 = Round_2()
                round_2.url = url
                round_2.status_code = '200'
                round_2.landing_page = browser.current_url
                round_2.landing_page_md5 = hashlib.md5(round_2.landing_page.encode('UTF-8')).hexdigest()
                round_2.checked = ''

                try:
                    save_name = screenshots_save_path + round_2.landing_page_md5 + '.png'
                    if not os.path.exists(save_name):
                        browser.save_screenshot(save_name)
                        print("截图成功")
                    else:
                        print("截图已存在")
                except BaseException as err_msg:
                    print("截图失败：%s" % err_msg)
                round_2.create_time = get_now_timestamp()
                session.add(round_2)
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
    browser.implicitly_wait(15)
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try:
        with open("url_round_1_todo.txt", "r", encoding="UTF8") as f:
            urls = f.readlines()
        for url in urls:
            url = url.strip()
            print('----------')
            rows = session.query(Round_2).filter(Round_2.url.like(url)).all()
            if rows:
                print("*** Already Visited. ***")
                continue
            visit(url, browser, session)
            # break  # for test
    except Exception as e:
        print("Error: ", e)
    finally:
        browser.close()
        browser.quit()
        session.close()
