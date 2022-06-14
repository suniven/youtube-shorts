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
from model import Virustotal_Domain, Virustotal_Domain_Detection, Virustotal_Domain_Details, Virustotal_Subdomain
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
virustotal_domain_prefix = 'https://www.virustotal.com/gui/domain/'


def wait_analyse(browser, count):  # 最多等待60s吧
    try:
        if count == 0:
            return
        js_numerator = 'return document.getElementsByTagName("domain-view")[0].shadowRoot.getElementById("report").shadowRoot.querySelector(".veredict-widget vt-ui-detections-widget").shadowRoot.querySelector(".positives")'
        control_in_shadow(browser, js_numerator)
        return
    except:
        time.sleep(6)
        count = count - 1
        wait_analyse(browser, count)


def control_in_shadow(browser, js):
    item = browser.execute_script(js)
    return item


def get_detection_result(browser, session, domain):
    try:
        virustotal_domain = Virustotal_Domain()
        virustotal_domain.domain = domain
        virustotal_domain.ratio = ''
        js_numerator = 'return document.getElementsByTagName("domain-view")[0].shadowRoot.getElementById("report").shadowRoot.querySelector(".veredict-widget vt-ui-detections-widget").shadowRoot.querySelector(".positives")'
        numerator = control_in_shadow(browser, js_numerator).text
        js_denominator = 'return document.getElementsByTagName("domain-view")[0].shadowRoot.getElementById("report").shadowRoot.querySelector(".veredict-widget vt-ui-detections-widget").shadowRoot.querySelector(".total")'
        denominator = control_in_shadow(browser, js_denominator).text.replace(" ", "")
        virustotal_domain.ratio = numerator + denominator
        # print("ratio: ", virustotal_domain.ratio)
        virustotal_domain.create_time = get_now_timestamp()
        session.add(virustotal_domain)
        session.commit()
    except Exception as err:
        print("*** virustotal_domain ratio err *** :", err)

    try:
        js_detections = 'return document.getElementsByTagName("domain-view")[0].shadowRoot.querySelector("vt-ui-detections-list").shadowRoot.querySelector("#detections")'
        detections = control_in_shadow(browser, js_detections)
        detection_list = detections.find_elements_by_css_selector('.detection')
        for detection in detection_list:
            vendor = detection.find_element_by_css_selector('.engine-name').text
            analysis = detection.find_element_by_css_selector('.individual-detection').text
            # print("{0}: {1}".format(vendor, analysis))
            virustotal_domain_detection = Virustotal_Domain_Detection()
            virustotal_domain_detection.domain = domain
            virustotal_domain_detection.subdomain = ''
            virustotal_domain_detection.vendor = vendor
            virustotal_domain_detection.analysis = analysis
            virustotal_domain_detection.type = 'domain'
            virustotal_domain_detection.create_time = get_now_timestamp()
            session.add(virustotal_domain_detection)
            session.commit()
    except Exception as err:
        print("*** virustotal_domain detection err *** :", err)


def get_details(browser, session, domain):
    try:
        js_detail = 'return document.getElementsByTagName("domain-view")[0].shadowRoot.getElementById("report").shadowRoot.querySelectorAll("vt-ui-button")[2]'
        detail_btn = control_in_shadow(browser, js_detail)
        detail_btn.click()
        js_cate = 'return document.getElementsByTagName("domain-view")[0].shadowRoot.querySelector("vt-ui-key-val-table").shadowRoot.querySelectorAll(".row")'
        cate_list = control_in_shadow(browser, js_cate)
        for cate in cate_list:
            engine = cate.find_element_by_css_selector('.label').text
            category = cate.find_element_by_css_selector('.value').text
            # print("{0}: {1}".format(engine, category))
            virustotal_domain_details = Virustotal_Domain_Details()
            virustotal_domain_details.domain = domain
            virustotal_domain_details.subdomain = ''
            virustotal_domain_details.engine = engine
            virustotal_domain_details.category = category
            virustotal_domain_details.type = 'domain'
            virustotal_domain_details.create_time = get_now_timestamp()
            session.add(virustotal_domain_details)
            session.commit()
    except Exception as err:
        print("*** virustotal_domain details err *** :", err)


def count_trs(browser):
    js_trs = 'return document.getElementsByTagName("domain-view")[0].shadowRoot.getElementById("relations").shadowRoot.querySelector(".subdomains").querySelector("vt-ui-generic-list").shadowRoot.querySelectorAll(".tr")'
    trs = control_in_shadow(browser, js_trs)
    # print(len(trs))
    return len(trs)


def load_more_subdomain(browser):
    try:
        pre = 0
        cur = count_trs(browser)
        flag = cur - pre
        while flag:
            print("loading...")
            js_load_btn = 'document.getElementsByTagName("domain-view")[0].shadowRoot.getElementById("relations").shadowRoot.querySelector(".subdomains").querySelector(".load-more").click()'
            browser.execute_script(js_load_btn)
            time.sleep(2)
            pre = cur
            cur = count_trs(browser)
            flag = cur - pre
    except:
        return


def find_subdomain(browser, js):
    try:
        browser.execute_script(js)
        return True
    except:
        return False


def get_subdomain(browser, session, domain):
    try:
        # 先判断有没有subdomain这个部分
        js_find_subdomain = 'return document.getElementsByTagName("domain-view")[0].shadowRoot.getElementById("relations").shadowRoot.querySelector(".subdomains")'
        if not find_subdomain(js_find_subdomain):
            print("** No subdomains. **")
            return

        js_relations = 'return document.getElementsByTagName("domain-view")[0].shadowRoot.getElementById("report").shadowRoot.querySelectorAll("vt-ui-button")[3]'
        relation_btn = control_in_shadow(browser, js_relations)
        relation_btn.click()

        load_more_subdomain()

        js_trs = 'return document.getElementsByTagName("domain-view")[0].shadowRoot.getElementById("relations").shadowRoot.querySelector(".subdomains").querySelector("vt-ui-generic-list").shadowRoot.querySelectorAll(".tr")'
        trs = control_in_shadow(browser, js_trs)
        for tr in trs:
            virustotal_subdomain = Virustotal_Subdomain()
            virustotal_subdomain.domain = domain
            virustotal_subdomain.subdomain = tr.find_elements_by_css_selector(".td")[0].text
            virustotal_subdomain.ratio = ''
            virustotal_subdomain.create_time = get_now_timestamp()
            session.add(virustotal_subdomain)
            session.commit()

    except Exception as err:
        print("*** virustotal_domain subdomain err *** :", err)


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

    f = open("../txt files/2-domain_in_comments.txt", "r", encoding="UTF8")
    domain_list = f.readlines()
    f.close()
    for domain in domain_list:
        domain = domain.strip('\n')
        if domain:
            rows = session.query(Virustotal_Domain).filter(Virustotal_Domain.domain.like(domain)).all()
            if rows:
                print("* Domain {0} Has Already Been Visited.".format(domain))
                continue
            print("--- Analysing {0} ---".format(domain))
            virustotal_domain_page = virustotal_domain_prefix + domain
            browser.get(virustotal_domain_page)
            time.sleep(2)
            wait_analyse(browser, 10)  # 软等待分析完成
            try:
                get_detection_result(browser, session, domain)
                get_details(browser, session, domain)
                get_subdomain(browser, session, domain)
                print("------")
            except:
                f = open("./domain_fail_log.txt", "a", encoding="UTF8")
                f.write(domain + '\n')
                f.close()
        # break  # for test
    browser.quit()
    session.close()
