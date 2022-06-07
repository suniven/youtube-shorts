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
from model import Virustotal_Url, Virustotal_Url_Detection, Virustotal_Url_Details
from bs4 import BeautifulSoup

sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
proxy = '127.0.0.1:1080'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
}
virustotal_url_page = 'https://www.virustotal.com/gui/url'


def get_detection_result(browser, session, url):
    search_input = browser.find_element_by_css_selector('#searchInput')
    search_input.send_keys(url)
    search_btn = browser.find_element_by_css_selector('#searchIcon')
    search_btn.click()
    time.sleep(5)
    virustotal_url = Virustotal_Url()
    virustotal_url.url = url
    virustotal_url.ratio = ''
    try:
        numerator = browser.find_element_by_css_selector('div > div > div.positives').text
        denominator = browser.find_element_by_css_selector('div > div > div.total').text
        virustotal_url.ratio = numerator + denominator
        print("ratio: ", virustotal_url.ratio)
    except Exception as err:
        print("*** virustotal_url err *** :", err)
    virustotal_url.create_time = get_now_timestamp()
    # session.add(virustotal_url)
    # session.commit()


def get_details(browser, session, url):
    return


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

    f = open("../txt files/landpage_in_comments.txt", "r", encoding="UTF8")
    url_list = f.readlines()
    f.close()
    for url in url_list:
        url = url.strip('\n')
        if url:
            print("--- Search {0} ---".format(url))
            browser.get(virustotal_url_page)
            time.sleep(1)
            get_detection_result(browser, session, url)
            get_details(browser, session, url)
            print("------")
        break  # for test
    browser.quit()
    session.close()
