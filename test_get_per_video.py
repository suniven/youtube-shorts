# 当前是youtube shorts版
# TODO: 考虑短视频和普通视频，统一截取视频标识用https://www.youtube.com/watch?v=____________访问
# TODO: 改一下wait方式
# TODO: 加一下video description的爬取

import model
import time
import re
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql


# MAX_COMMENT_COUNT = 100     # 爬取的最大评论数量

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


def insert_db(item):
    # 哪个天才设计的数据库索引长度限制
    # 初始化数据库连接
    engine = create_engine('mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4', echo=True,
                           max_overflow=8)

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    session.add(item)
    session.commit()
    session.close()


def get_video_comments(browser, video):
    browser.find_element_by_css_selector('div#comments-button>ytd-button-renderer>a.ytd-button-renderer').click()
    time.sleep(1)

    # 评论数量
    video.comments_count = int(browser.find_element_by_css_selector(
        'div#title-container>h2#title>yt-formatted-string#contextual-info').text)
    print('comments count: ', video.comments_count)

    # 抓取评论
    # 滚动加载评论
    mouse = browser.find_element_by_css_selector('div#placeholder-area')
    ActionChains(browser).move_to_element(mouse)

    ex_height = 0
    flag = 1
    while flag:
        browser.execute_script('window.scrollBy(0,5000)')
        container = browser.find_element_by_css_selector('ytd-item-section-renderer#sections')
        height = container.size['height']
        flag = height - ex_height
        ex_height = height
        print(flag)
        time.sleep(2)

    # 关闭评论页面
    close_btn = browser.find_element_by_css_selector('div#visibility-button')
    time.sleep(1)
    ActionChains(browser).move_to_element(close_btn).click(close_btn).perform()
    time.sleep(1)


def get_video_info(browser, video_item):
    video = model.Video()
    video.video_link = video_item.get_attribute('href')
    video.video_id = video.video_link[-11:]
    video_item.click()
    time.sleep(6)

    video.title = video_item.get_attribute('title')
    video.publisher = browser.find_element_by_xpath('//*[@id="text"]/a').text
    print('publisher: ', video.publisher)
    video.publisher_link = browser.find_element_by_xpath('//*[@id="channel-info"]/a').get_attribute('href')
    print('publisher homepage: ', video.publisher_link)
    print('video_id: ', video.video_id)

    # 抓评论
    get_video_comments(browser, video)
    time.sleep(1)

    # 详情按钮
    # 注意这个万恶按钮的元素定位
    detail_btn = browser.find_element_by_css_selector('div#actions>div#menu>ytd-menu-renderer>yt-icon-button#button')
    time.sleep(1)
    ActionChains(browser).move_to_element(detail_btn).click(detail_btn).perform()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="items"]/ytd-menu-service-item-renderer/tp-yt-paper-item').click()
    time.sleep(1)

    video.date = browser.find_element_by_xpath('//*[@id="publish-time"]/span[1]').text
    print('publish date: ', video.date)
    views = re.sub(',', '', browser.find_element_by_xpath('//*[@id="view-count"]/yt-formatted-string/span[1]').text)
    video.views = int(views)
    print('views: ', video.views)

    # TODO: 视频描述 需要先判断description是否存在
    description=browser.find_elements_by_xpath('//*[@id="description"]/span')

    insert_db(video)


if __name__ == '__main__':
    publisher_link = 'https://www.youtube.com/channel/UCbd0IJ1OJAVcjjEH4t9VjEw/videos'
    browser = webdriver.Chrome()
    try:
        browser.get(publisher_link)

        time.sleep(4)
        video_list = browser.find_element_by_id('video-title')
        get_video_info(browser, video_list)

    finally:
        browser.close()
