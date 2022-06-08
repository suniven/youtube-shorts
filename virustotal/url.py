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


def wait_analyse(browser, count):  # 最多等待60s吧
    try:
        if count == 0:
            return
        js_numerator = 'return document.getElementsByTagName("url-view")[0].shadowRoot.getElementById("report").shadowRoot.querySelector(".veredict-widget vt-ui-detections-widget").shadowRoot.querySelector(".positives")'
        control_in_shadow(browser, js_numerator)
        return
    except:
        time.sleep(6)
        count = count - 1
        wait_analyse(browser, count)


def control_in_shadow(browser, js):
    item = browser.execute_script(js)
    return item


def get_detection_result(browser, session, url):
    js_search_input = 'return document.getElementsByTagName("vt-ui-shell")[0].shadowRoot.getElementById("searchbar").shadowRoot.getElementById("searchInput")'
    search_input = control_in_shadow(browser, js_search_input)
    search_input.send_keys(url)
    js_search_btn = 'return document.getElementsByTagName("vt-ui-shell")[0].shadowRoot.getElementById("toolbar").shadowRoot.getElementById("searchIcon")'
    search_btn = control_in_shadow(browser, js_search_btn)
    search_btn.click()
    time.sleep(3)

    # URL分析可能要比较久
    wait_analyse(browser, 10)

    virustotal_url = Virustotal_Url()
    virustotal_url.url = url
    virustotal_url.ratio = ''
    try:
        js_numerator = 'return document.getElementsByTagName("url-view")[0].shadowRoot.getElementById("report").shadowRoot.querySelector(".veredict-widget vt-ui-detections-widget").shadowRoot.querySelector(".positives")'
        numerator = control_in_shadow(browser, js_numerator).text
        js_denominator = 'return document.getElementsByTagName("url-view")[0].shadowRoot.getElementById("report").shadowRoot.querySelector(".veredict-widget vt-ui-detections-widget").shadowRoot.querySelector(".total")'
        denominator = control_in_shadow(browser, js_denominator).text.replace(" ", "")
        virustotal_url.ratio = numerator + denominator
        print("ratio: ", virustotal_url.ratio)
    except Exception as err:
        print("*** virustotal_url ratio err *** :", err)
    virustotal_url.create_time = get_now_timestamp()
    session.add(virustotal_url)
    session.commit()

    try:
        js_detections = 'return document.getElementsByTagName("url-view")[0].shadowRoot.querySelector("vt-ui-detections-list").shadowRoot.querySelector("#detections")'
        detections = control_in_shadow(browser, js_detections)
        detection_list = detections.find_elements_by_css_selector('.detection')
        rows = session.query(Virustotal_Url).filter(Virustotal_Url.url.like(url)).all()
        url_id = rows[0].id
        for detection in detection_list:
            vendor = detection.find_element_by_css_selector('.engine-name').text
            analysis = detection.find_element_by_css_selector('.individual-detection').text
            # print("{0}: {1}".format(vendor, analysis))
            virustotal_url_detection = Virustotal_Url_Detection()
            virustotal_url_detection.url = url
            virustotal_url_detection.url_id = url_id
            virustotal_url_detection.vendor = vendor
            virustotal_url_detection.analysis = analysis
            virustotal_url_detection.create_time = get_now_timestamp()
            session.add(virustotal_url_detection)
            session.commit()
    except Exception as err:
        print("*** virustotal_url detection err *** :", err)


def get_details(browser, session, url):
    js_detail = 'return document.getElementsByTagName("url-view")[0].shadowRoot.getElementById("report").shadowRoot.querySelectorAll("vt-ui-button")[2]'
    detail_btn = control_in_shadow(browser, js_detail)
    detail_btn.click()
    rows = session.query(Virustotal_Url).filter(Virustotal_Url.url.like(url)).all()
    url_id = rows[0].id
    js_cate = 'return document.getElementsByTagName("url-view")[0].shadowRoot.getElementById("details").shadowRoot.querySelector("vt-ui-expandable span vt-ui-key-val-table").shadowRoot.querySelectorAll(".row")'
    cate_list = control_in_shadow(browser, js_cate)
    for cate in cate_list:
        engine = cate.find_element_by_css_selector('.label').text
        category = cate.find_element_by_css_selector('.value').text
        # print("{0}: {1}".format(engine, category))
        virustotal_url_details = Virustotal_Url_Details()
        virustotal_url_details.url_id = url_id
        virustotal_url_details.url = url
        virustotal_url_details.engine = engine
        virustotal_url_details.category = category
        virustotal_url_details.create_time = get_now_timestamp()
        session.add(virustotal_url_details)
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

    f = open("../txt files/landpage_in_comments.txt", "r", encoding="UTF8")
    url_list = f.readlines()
    f.close()
    for url in url_list:
        url = url.strip('\n')
        if url:
            rows = session.query(Virustotal_Url).filter(Virustotal_Url.url.like(url)).all()
            if rows:
                print("* URL {0} Has Already Been Visited.".format(url))
                continue
            print("--- Search {0} ---".format(url))
            browser.get(virustotal_url_page)
            time.sleep(2)
            try:
                get_detection_result(browser, session, url)
                get_details(browser, session, url)
                print("------")
            except:
                f = open("./fail_log.txt", "a", encoding="UTF8")
                f.write(url + '\n')
                f.close()
        # break  # for test
    browser.quit()
    session.close()
