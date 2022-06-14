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
from model import Virustotal_Domain_Detection, Virustotal_Domain_Details, Virustotal_Subdomain

sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
virustotal_domain_prefix = 'https://www.virustotal.com/gui/domain/'


def control_in_shadow(browser, js):
    item = browser.execute_script(js)
    return item


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


def get_detection_result(browser, session, subdomain):
    try:
        js_numerator = 'return document.getElementsByTagName("domain-view")[0].shadowRoot.getElementById("report").shadowRoot.querySelector(".veredict-widget vt-ui-detections-widget").shadowRoot.querySelector(".positives")'
        numerator = control_in_shadow(browser, js_numerator).text
        js_denominator = 'return document.getElementsByTagName("domain-view")[0].shadowRoot.getElementById("report").shadowRoot.querySelector(".veredict-widget vt-ui-detections-widget").shadowRoot.querySelector(".total")'
        denominator = control_in_shadow(browser, js_denominator).text.replace(" ", "")
        ratio = numerator + denominator
        session.query(Virustotal_Subdomain).filter(Virustotal_Subdomain.subdomain.like(subdomain)).update(
            {'ratio': ratio}, synchronize_session=False)
        # print("ratio: ", virustotal_domain.ratio)
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
            virustotal_domain_detection.domain = '.'.join(subdomain.split('.')[-2:])
            virustotal_domain_detection.subdomain = subdomain
            virustotal_domain_detection.vendor = vendor
            virustotal_domain_detection.analysis = analysis
            virustotal_domain_detection.type = 'subdomain'
            virustotal_domain_detection.create_time = get_now_timestamp()
            session.add(virustotal_domain_detection)
            session.commit()
    except Exception as err:
        print("*** virustotal_subdomain detection err *** :", err)


def get_details(browser, session, subdomain):
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
            virustotal_domain_details.domain = '.'.join(subdomain.split('.')[-2:])
            virustotal_domain_details.subdomain = subdomain
            virustotal_domain_details.engine = engine
            virustotal_domain_details.category = category
            virustotal_domain_details.type = 'subdomain'
            virustotal_domain_details.create_time = get_now_timestamp()
            session.add(virustotal_domain_details)
            session.commit()
    except Exception as err:
        print("*** virustotal_domain details err *** :", err)


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

    rows = session.query(Virustotal_Subdomain).filter().all()
    for row in rows:
        subdomain = row.subdomain
        rows = session.query(Virustotal_Subdomain).filter(
            Virustotal_Subdomain.subdomain.like(subdomain)).all()
        if rows[0].ratio:
            print("* SubDomain {0} Has Already Been Visited.".format(subdomain))
            continue
        print("--- Analysing {0} ---".format(subdomain))
        virustotal_subdomain_page = virustotal_domain_prefix + subdomain
        browser.get(virustotal_subdomain_page)
        time.sleep(2)
        wait_analyse(browser, 10)  # 软等待分析完成
        try:
            get_detection_result(browser, session, subdomain)
            get_details(browser, session, subdomain)
            print("------")
        except:
            f = open("./domain_fail_log.txt", "a", encoding="UTF8")
            f.write(subdomain + '\n')
            f.close()
        # break  # for test
    browser.quit()
    session.close()
