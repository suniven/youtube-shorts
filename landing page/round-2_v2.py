import re
import os
import time
import requests
import hashlib
import logging
from model import Round_2_New
from timestamp import datetime_timestamp, timestamp_datetime, get_now_timestamp
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy.sql import and_, asc, desc, or_
from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker

file_save_root_path = './v2_singapore/'
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
MAX_DEEPTH = 3
filter_keyword = ["google.com", "youtube.com"]


def visit(browser, url, deepth, results):
    print("visit: ", url)
    browser.get(url)
    url_domain = url.split('/')[2]
    current_domain = browser.current_url.split('/')[2]
    if deepth >= MAX_DEEPTH or url_domain == current_domain:
        return
    else:
        results.append(browser.current_url)
        try:
            atags = browser.find_elements_by_tag_name('a')
        except:
            return
        links = []
        for atag in atags:
            try:
                if 'http' in atag.get_attribute('href'):
                    links.append(atag.get_attribute('href'))
            except:
                continue
        if links:
            links = list(set(links))
            # print(len(links))
            for link in links:
                # print("link: ", link)
                if "google.com" in link or "youtube.com" in link or "facebook.com" in link:
                    continue
                visit(browser, link, deepth + 1, results)
        else:
            return


if __name__ == '__main__':
    # logger.debug('----调试信息 [debug]------')
    # logger.info('[info]')
    # logger.warning('警告信息[warning]')
    # logger.error('错误信息[error]')
    # logger.critical('严重错误信息[crtical]')

    # browser = webdriver.Chrome()
    # browser.maximize_window()
    # headless模式
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument("--window-size=1920,1080")
    option.add_argument("--mute-audio")  # 静音
    browser = webdriver.Chrome(chrome_options=option)
    browser.implicitly_wait(20)

    try:
        with open("url_round_2_todo.txt", "r", encoding="UTF8") as f:
            items = f.readlines()
        for item in items:
            url = item.strip()
            file_save_path = file_save_root_path + hashlib.md5(url.encode('UTF-8')).hexdigest() + ".txt"
            if os.path.exists(file_save_path):
                print("文件已存在")
                continue
            results = []
            results.append(url)
            visit(browser, url, 1, results)

            with open(file_save_path, "w", encoding="UTF8") as f:
                for result in results:
                    f.write(result + '\n')
    except Exception as e:
        print("*err: ", e)
    finally:
        browser.close()
        browser.quit()
