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

yt_url_prefix = 'https://www.youtube.com/watch?v='  # 方便拉评论
MAX_SCROLL_COUNT = 400  # 检查评论时页面下拉最大次数 同时下拉评论可以顺便解决自动连播的问题


def scroll(browser):
    ex_height = 0
    flag = 1
    for i in range(MAX_SCROLL_COUNT):
        if flag:
            browser.execute_script('window.scrollBy(0,5000)')
            comment = browser.find_element_by_css_selector('#comments')
            height = comment.size['height']
            flag = height - ex_height
            ex_height = height
            time.sleep(2)


def check_comment(content):
    return True


def check_video_comments(browser):
    time.sleep(2)
    print("Visiting Video: ", browser.current_url)
    scroll(browser)
    comments_containers = browser.find_elements_by_css_selector('#contents > ytd-comment-thread-renderer')
    print("Comments Count: ", len(comments_containers))
    for comments_container in comments_containers:
        content = comments_container.find_element_by_css_selector('#content-text').text
        check_comment(content)
        # print(content)

    print('--------------------------')


if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.maximize_window()
    try:
        browser.get('https://www.youtube.com/')
        browser.find_element_by_css_selector('#items > ytd-guide-entry-renderer:nth-child(3)').click()
        time.sleep(3)
        main_handle = browser.current_window_handle

        while True:
            try:
                video_id = browser.current_url[-11:]
                video_url = yt_url_prefix + video_id
                js = 'window.open(\"' + video_url + '\");'
                # print("js: ", js)
                browser.execute_script(js)
                handles = browser.window_handles
                # print("Handles Count: ", len(browser.window_handles))
                browser.switch_to.window(handles[1])
                time.sleep(4)
                check_video_comments(browser)
            except Exception as e:
                print("Error: ", e)
            finally:
                browser.close()
                # print("After Closing...\nHandles Count: ", len(browser.window_handles))
                browser.switch_to.window(main_handle)
                time.sleep(2)
                browser.find_element_by_css_selector('#navigation-button-down > ytd-button-renderer > a').click()
    except Exception as e:
        print("Error: ", e)
    finally:
        browser.close()
        browser.quit()
