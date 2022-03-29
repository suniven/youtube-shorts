import model
import time
import re
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


# YouTube的有时候提取不到url，打算试试直接用http://i.ytimg.com/vi/_________(vid)/hq2.jpg访问提取


def scroll(driver):
    ex_height = 0
    flag = 1
    while flag:
        driver.execute_script('window.scrollBy(0,5000)')
        page = driver.find_element_by_id('page-manager')
        height = page.size['height']
        flag = height - ex_height
        ex_height = height
        # print(flag)
        time.sleep(4)

    # while height > 0:
    #     driver.execute_script('window.scrollBy(0,-800)')
    #     height = height - 800


# link eg. https://www.youtube.com/channel/UCbd0IJ1OJAVcjjEH4t9VjEw/videos'
def get_yt_cover(vid):
    img_path = './cover_img/yt/' + vid + '.jpg'
    img_url = 'http://i.ytimg.com/vi/' + vid + '/hq2.jpg'  # 注意别https

    try:
        r = requests.get(img_url, timeout=2)
        r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
    except requests.RequestException as e:
        print(e)
    else:
        with open(img_path, 'wb') as f:
            f.write(r.content)


def get_tt_cover(driver, link):
    return


if __name__ == '__main__':
    publisher_link = 'https://www.youtube.com/channel/UCbd0IJ1OJAVcjjEH4t9VjEw/videos'
    browser = webdriver.Chrome()
    try:
        browser.get(publisher_link)
        time.sleep(4)
        scroll(browser)
        video_title = browser.find_elements_by_id('video-title')
        print('Total Count: ', len(video_title))  # 一次是30个视频

        for item in video_title:
            video_link = item.get_attribute('href')
            video_id = video_link[-11:]
            get_yt_cover(video_id)

    finally:
        browser.close()
