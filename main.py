import requests
import lxml
import time
import model
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 滑动到底部
def scroll(driver):
    ex_height = 0
    flag = 1
    while flag:
        driver.execute_script('window.scrollBy(0,5000)')
        page = driver.find_element_by_id('page-manager')
        height = page.size['height']
        flag = height - ex_height
        ex_height = height
        print(flag)
        time.sleep(3)


if __name__ == '__main__':
    publisher_link = 'https://www.youtube.com/channel/UCbd0IJ1OJAVcjjEH4t9VjEw/videos'
    browser = webdriver.Chrome()
    try:
        browser.get(publisher_link)

        time.sleep(3)
        scroll(browser)
        video_title = browser.find_elements_by_id('video-title')
        print('Total Count: ', len(video_title))  # 一次是30个视频

        for item in video_title:
            item.click()

    finally:
        browser.close()
