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


def get_comments(browser, comments_btn):
    comments_btn.click()
    time.sleep(2)
    

def get_video_info(browser, video_item):
    video = model.Video()
    video.video_link = video_item.get_attribute('href')

    video_item.click()
    time.sleep(6)

    video.title = video_item.get_attribute('title')
    video.publisher = browser.find_element_by_xpath('//*[@id="text"]/a').text
    print('publisher: ', video.publisher)
    video.publisher_link = browser.find_element_by_xpath('//*[@id="channel-info"]/a').get_attribute('href')
    print('publisher homepage: ', video.publisher_link)

    # 抓评论
    comments_btn = browser.find_element_by_css_selector('div#comments-button>ytd-button-renderer>a.ytd-button-renderer')
    time.sleep(1)
    get_comments(browser, comments_btn)

    # 详情按钮
    # 注意这个按钮的元素定位
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

    # 哪个天才设计的数据库索引长度限制
    # 初始化数据库连接
    engine = create_engine('mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4', echo=True,
                           max_overflow=8)
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)
    # 实例化session对象:
    session = DBSession()
    # 添加到session
    session.add(video)
    # 提交即保存到数据库
    session.commit()
    # 关闭session
    session.close()


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
