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
sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/yt?charset=utf8mb4'
yt_url_prefix = 'https://www.youtube.com/watch?v='  # 方便拉评论
MAX_SCROLL_COUNT = 200  # 检查评论时页面下拉最大次数 同时下拉评论可以顺便解决自动连播的问题 250大概可以加载3k条？
MAX_GET_COUNT = 20000  # 往下刷2w个视频


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
            time.sleep(1.5)


def check_comment(content):
    links = re.findall(r'((?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})+(?:(?:\/[=\w\?]+)*))+',
                       content)
    if links:
        return True
    else:
        return False


def check_video_comments(browser, session):
    print("Visiting Video: ", browser.current_url)
    browser.execute_script('window.scrollBy(0,800)')  # 保证评论可以加载出来
    time.sleep(1)
    scroll(browser)
    comments_containers = browser.find_elements_by_css_selector('#contents > ytd-comment-thread-renderer')
    print("Comments Count: ", len(comments_containers))
    for comments_container in comments_containers:
        content = comments_container.find_element_by_css_selector('#content-text').text
        # print(content)
        if check_comment(content):
            comment = model.Comment()
            comment.content = content
            comment.video_id = browser.current_url[-11:]
            comment.user = comments_container.find_element_by_css_selector('#author-text').text
            comment.type = 2
            comment.user_link = comments_container.find_element_by_css_selector('#author-text').get_attribute('href')
            comment.date = comments_container.find_element_by_css_selector('.published-time-text').text
            comment.create_time = get_now_timestamp()

            print(comment.video_id)
            print(comment.user)
            print(comment.user_link)
            print(comment.content)
            print(comment.date)
            print(comment.create_time)

            session.add(comment)
            session.commit()

    print('--------------------------')


if __name__ == '__main__':
    # # 正常模式
    # browser = webdriver.Chrome()
    # browser.maximize_window()
    # headless模式
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument("--window-size=1920,1080")
    option.add_argument("--mute-audio") # 静音
    browser = webdriver.Chrome(chrome_options=option)
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    browser.get('https://www.youtube.com/')
    browser.find_element_by_css_selector('#items > ytd-guide-entry-renderer:nth-child(3)').click()
    time.sleep(4)
    main_handle = browser.current_window_handle

    while True:
        # MAX_GET_COUNT = MAX_GET_COUNT - 1
        try:
            video_id = browser.current_url[-11:]
            print("video_id: ", video_id)
            # 检查是否已经爬取过这个视频的评论了
            rows = session.query(model.Comment).filter(model.Comment.video_id.like(video_id)).all()
            print("rows: ", len(rows))
            if not rows:
                comment = model.Comment()
                comment.content = ''
                comment.video_id = video_id
                comment.user = ''
                comment.type = -1   # 占位
                comment.user_link = ''
                comment.date = ''
                comment.create_time = get_now_timestamp()
                session.add(comment)
                session.commit()

                video_url = yt_url_prefix + video_id
                js = 'window.open(\"' + video_url + '\");'
                # print("js: ", js)
                browser.execute_script(js)
                handles = browser.window_handles
                # print("Handles Count: ", len(browser.window_handles))
                browser.switch_to.window(handles[1])
                time.sleep(4)
                check_video_comments(browser, session)
                browser.close()
                # print("After Closing...\nHandles Count: ", len(browser.window_handles))
                browser.switch_to.window(main_handle)
                time.sleep(2)
        except Exception as e:
            print("Error: ", e)
        finally:
            print("Get Next Video...")
            print(print(timestamp_datetime(time.time())))
            browser.find_element_by_css_selector('#navigation-button-down > ytd-button-renderer > a').click()
            time.sleep(3)   # 保证加载出来下个视频
            # break  # for test

    browser.close()
    browser.quit()
    session.close()
