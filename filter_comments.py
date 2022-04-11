# TODO: 统计评论中包含色情链接的数量
# TODO: 将包含色情链接的评论打上tag
# 保存落地页的相关信息 eg. title 截图
# TODO: 将发布此类评论的用户打上tag并统计每名用户发了多少条此类评论
# 访问色情链接，保存跳转后的落地页链接

from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy import text
from model import Comment, Site
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import re
import os
import requests

sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
proxy = '127.0.0.1:1080'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
}


def judge_comment(comment, broswer):
    links = re.findall(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', comment.content)
    print(comment.id, comment.user_link[-24:], links)

    cnt = 0
    for link in links:
        try:
            res = requests.get('http://' + link, headers=headers, timeout=8, proxies=proxies)
            print("Visiting Site: http://%s" % link)
            print("Status Code: %s" % res.status_code)
            if res.status_code != 200:
                print("响应失败")
                print("-----------------------------")
            else:
                browser.get('http://' + link)
                print("响应成功")
                if browser.title:
                    title = browser.title
                else:
                    title = ''

                try:
                    screenshot = '.\\screenshots\\' + str(comment.id) + '_' + str(cnt) + '.png'
                    browser.save_screenshot(screenshot)
                    print("截图成功")
                except BaseException as err_msg:
                    print("截图失败：%s" % err_msg)

                print("-----------------------------")
                land_page = browser.current_url
                site = Site()
                site.user_id = comment.user_link[-24:]
                site.comment_id = comment.id
                site.land_page = land_page
                site.url = link
                site.page_title = title
                site.screenshot = './screenshots/' + str(comment.id) + '_' + str(cnt) + '.png'
                cnt = cnt + 1

                # 插入数据库
                engine = create_engine(sqlconn, echo=True, max_overflow=8)
                DBSession = sessionmaker(bind=engine)
                session = DBSession()
                session.add(site)
                session.commit()
                session.close()
        except Exception as e:
            print("Err: ", e)


if __name__ == '__main__':
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    comments = session.query(Comment).filter(
        Comment.content.op('regexp')(r'([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}')).all()
    session.close()

    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=option)
    print("len: ", len(comments))
    for comment in comments:
        if comment.id == 20568:
            judge_comment(comment, browser)
    browser.quit()
