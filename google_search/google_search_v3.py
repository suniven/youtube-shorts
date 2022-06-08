# 自己写的selenium + programmable search engine

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
from model import Google_Search_Result
from bs4 import BeautifulSoup

search_engine_url = 'https://cse.google.com/cse?cx=a7dbc3e35111d44eb'
sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
proxy = '127.0.0.1:1080'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
}


def get_search_result(query, browser, session):
    search_input = browser.find_element_by_css_selector('#gsc-i-id1')
    search_input.send_keys(query)
    search_btn = browser.find_element_by_css_selector('button.gsc-search-button')
    search_btn.click()
    time.sleep(5)

    try:
        try:
            gsc_cursor = browser.find_element_by_css_selector('div.gsc-cursor')
            page_count = len(gsc_cursor.find_elements_by_tag_name('div'))
        except Exception as err:
            page_count = 1  # 只有一页结果 没有翻页
            print(err)
        for i in range(page_count):
            # 容易点击了第一个翻页之后，页面出现刷新的情况 导致stale element reference: element is not attached to the page document
            if i != 0:
                # 或者用xpath[i+1] 不想写了
                gsc_cursor = browser.find_element_by_css_selector('div.gsc-cursor')
                page = gsc_cursor.find_elements_by_tag_name('div')[i]
                ActionChains(browser).move_to_element(page).click().perform()
                # pages[i].click()
                time.sleep(5)

            results = browser.find_elements_by_css_selector('div.gsc-expansionArea > div.gsc-webResult')
            for result in results:
                google_search_result = Google_Search_Result()
                google_search_result.query = query.replace("\"", "")
                google_search_result.title = ""
                google_search_result.url = ""
                google_search_result.snippet = ""

                google_search_result.title = result.find_element_by_css_selector('div.gs-title').text
                google_search_result.url = result.find_element_by_css_selector('a.gs-title').get_attribute(
                    'data-ctorig')
                google_search_result.snippet = result.find_element_by_css_selector('div.gsc-table-result').text
                google_search_result.create_time = get_now_timestamp()
                session.add(google_search_result)
                session.commit()

    except Exception as err_msg:
        print("** Error: ", err_msg)
        f_err = open("./error_log_v3.txt", "a", encoding="UTF8")
        f_err.write("Error: Query {0}\tErrMsg: {1}\n".format(query, err_msg))
        f_err.close()


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

    f = open("../txt files/url_in_comments.txt", "r", encoding="UTF8")
    # f = open("../txt files/for_test.txt", "r", encoding="UTF8")
    url_list = f.readlines()
    f.close()
    browser.get(search_engine_url)
    time.sleep(3)
    for url in url_list:
        url = url.strip('\n')
        if url:
            kw = "\"" + url + "\""
            print("-- Query: {0} --".format(kw))
            rows = session.query(Google_Search_Result).filter(
                Google_Search_Result.query.like(kw.replace("\"", ""))).all()
            if rows:
                continue
            get_search_result(kw, browser, session)
            browser.refresh()
            time.sleep(8)

    browser.quit()
    session.close()
