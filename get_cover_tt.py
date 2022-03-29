import model
import time
import re
import requests
import cssselect
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

MAX_COUNT = 100


# 往下加载MAX_COUNT次
def scroll(driver):
    for i in range(MAX_COUNT):
        driver.execute_script('window.scrollBy(0,5000)')
        time.sleep(3)


if __name__ == '__main__':
    # MAX_COUNT = 100  # 继续加载100次，即101*12=1212个视频
    # publisher_link = 'https://www.tiktok.com/search?q=wear%20it%20big%20challenge&t=1648532403284'
    # browser = webdriver.Chrome()
    # try:
    #     browser.get(publisher_link)
    #     time.sleep(4)
    #
    #     for i in range (MAX_COUNT):
    #         btn=browser.find_element_by_css_selector('button.tiktok-1mwtjmv-ButtonMore')
    #         btn.click()
    #         time.sleep(4)
    #
    #     imgs = browser.find_elements_by_css_selector('img.tiktok-1itcwxg-ImgPoster')
    #     for img in imgs:
    #         print(img.get_attribute('src'))
    #
    #
    # finally:
    #     browser.close()

    publisher_link = 'https://www.tiktok.com/tag/wearitbigchallenge'
    browser = webdriver.Chrome()
    try:
        browser.get(publisher_link)
        time.sleep(4)
        scroll(browser)

        items = browser.find_elements_by_css_selector('div.tiktok-yz6ijl-DivWrapper')
        for item in items:
            html = item.get_attribute('innerHTML')
            # print(html)
            html = etree.HTML(html)
            video_link = html.cssselect('a')[0].attrib['href']
            img_name = re.sub('\/', '-', video_link[24:])  # 回溯视频时将'-'换回'/'加上前缀即可访问原视频
            print(img_name)

            img_path = './cover_img/tt/' + img_name + '.jpg'

            img_link = html.cssselect('img')[0].attrib['src']
            img_link = 'http' + img_link[5:]
            print(img_link)

            try:
                r = requests.get(img_link, timeout=2)
                r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
            except requests.RequestException as e:
                print(e)
            else:
                with open(img_path, 'wb') as f:
                    f.write(r.content)

        # imgs = browser.find_elements_by_css_selector('img.tiktok-1itcwxg-ImgPoster')
        #
        # for img in imgs:
        #     img_path = './cover_img/tt/' + vid + '.jpg'
        #     img_url = 'http' + img.get_attribute('src')[5:]
        #
        #     try:
        #         r = requests.get(img_url, timeout=2)
        #         r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
        #     except requests.RequestException as e:
        #         print(e)
        #     else:
        #         with open(img_path, 'wb') as f:
        #             f.write(r.content)


    finally:
        browser.close()
