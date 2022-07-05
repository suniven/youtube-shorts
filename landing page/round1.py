import re
import time
import model
from timestamp import datetime_timestamp, timestamp_datetime, get_now_timestamp
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql

# sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
yt_url_prefix = 'https://www.youtube.com/watch?v='  # 方便拉评论
MAX_SCROLL_COUNT = 200  # 检查评论时页面下拉最大次数 同时下拉评论可以顺便解决自动连播的问题 250大概可以加载3k条？
MAX_GET_COUNT = 20000  # 往下刷2w个视频

if __name__ == '__main__':
    # # 正常模式
    # browser = webdriver.Chrome()
    # browser.maximize_window()
    # headless模式
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument("--window-size=1920,1080")
    option.add_argument("--mute-audio")  # 静音
    browser = webdriver.Chrome(chrome_options=option)

    browser.get('https://www.youtube.com/')


    try:
        while True:
            # MAX_GET_COUNT = MAX_GET_COUNT - 1
            try:
                video_id = browser.current_url[-11:]
                print("video_id: ", video_id)
                # 检查是否已经爬取过这个视频的评论了


            except Exception as e:
                print("Error: ", e)
            finally:
                print("Get Next Video...")
                print(print(timestamp_datetime(time.time())))
                browser.find_element_by_css_selector('#navigation-button-down > ytd-button-renderer > a').click()
                time.sleep(3)  # 保证加载出来下个视频
                # break  # for test
    except Exception as e:
        print("Error: ", e)
    finally:
        browser.quit()
        session.close()