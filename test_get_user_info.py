# TODO: 判断重复插入

import model
import time
import re
import cssselect
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql


def test(driver, line):
    print("-------------------")
    user = model.User()
    user.links = ""
    user.views = 0
    user.description = ""
    user.type = 0
    user.details = ""
    user.homepage = line
    user.join_time = ""
    user.subscribers = 0
    user.username = ""
    user.user_id = line[-24:]

    username = driver.find_element_by_css_selector(
        'ytd-channel-name.ytd-c4-tabbed-header-renderer > div:nth-child(1) > div:nth-child(1) > yt-formatted-string:nth-child(1)').text
    user.username = username

    try:
        views = driver.find_element_by_css_selector(
            'yt-formatted-string.ytd-channel-about-metadata-renderer:nth-child(3)').text
        views = int(''.join(filter(str.isdigit, views)))
        user.views = views
    except:
        print("views error")

    try:
        description = driver.find_element_by_css_selector(
            '#description-container > yt-formatted-string:nth-child(2)').text
        user.description = description
    except:
        print("description error")

    try:
        links = driver.find_elements_by_css_selector('#link-list-container>a')
        for link in links:
            link = link.get_attribute('href')
            user.links = user.links + link + "\n"
    except:
        print("link error")

    try:
        # bug fix
        details_container = driver.find_element_by_css_selector('#details-container')
        html = details_container.get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'lxml')
        # text = soup.find_all('yt-formatted-string')
        # for item in text:
        #     details = details + item.text
        details = soup.find('table').text
        details = ''.join(details.split('\n'))
        user.details = details
    except Exception as e:
        print("details error: ", e)

    try:
        join_time = driver.find_element_by_css_selector(
            '#right-column > yt-formatted-string:nth-child(2) > span:nth-child(1)').text
        user.join_time = join_time
    except:
        print("join_time error")

    try:
        subscribers = driver.find_element_by_css_selector('yt-formatted-string#subscriber-count').text
        subscribers = int(''.join(filter(str.isdigit, subscribers)))
        user.subscribers = subscribers
    except:
        print("subscribers error")

    print(user.details)
    print("-------------------")


def get_user_info(driver, line, session):
    user = model.User()
    user.links = ""
    user.views = 0
    user.description = ""
    user.type = 0
    user.details = ""
    user.homepage = line
    user.join_time = ""
    user.subscribers = 0
    user.username = ""
    user.user_id = line[-24:]

    username = driver.find_element_by_css_selector(
        'ytd-channel-name.ytd-c4-tabbed-header-renderer > div:nth-child(1) > div:nth-child(1) > yt-formatted-string:nth-child(1)').text
    user.username = username

    try:
        views = driver.find_element_by_css_selector(
            'yt-formatted-string.ytd-channel-about-metadata-renderer:nth-child(3)').text
        views = int(''.join(filter(str.isdigit, views)))
        user.views = views
    except:
        print("views error")

    try:
        description = driver.find_element_by_css_selector(
            '#description-container > yt-formatted-string:nth-child(2)').text
        user.description = description
    except:
        print("description error")

    try:
        links = driver.find_elements_by_css_selector('#link-list-container>a')
        for link in links:
            link = link.get_attribute('href')
            user.links = user.links + link + "\n"
    except:
        print("link error")

    try:
        # bug fix
        details_container = driver.find_element_by_css_selector('#details-container')
        html = details_container.get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'lxml')
        # text = soup.find_all('yt-formatted-string')
        # for item in text:
        #     details = details + item.text
        details = soup.find('table').text
        details = ''.join(details.split('\n'))
        user.details = details
    except Exception as e:
        print("details error: ", e)

    try:
        join_time = driver.find_element_by_css_selector(
            '#right-column > yt-formatted-string:nth-child(2) > span:nth-child(1)').text
        user.join_time = join_time
    except:
        print("join_time error")

    try:
        subscribers = driver.find_element_by_css_selector('yt-formatted-string#subscriber-count').text
        subscribers = int(''.join(filter(str.isdigit, subscribers)))
        user.subscribers = subscribers
    except:
        print("subscribers error")

    session.add(user)
    session.commit()


if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4', echo=True,
                           max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    f = open("./user_link.txt", encoding='UTF-8')
    lines = f.readlines()
    lines = list(set(lines))  # 去重
    print(len(lines))
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=option)

    for line in lines:
        line = line.strip('\n')
        print(line)
        publisher_link = line + '/about'

        browser.get(publisher_link)
        time.sleep(5)
        get_user_info(browser, line, session)

    f.close()
    browser.quit()
    session.close()
