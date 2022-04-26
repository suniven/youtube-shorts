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
from sqlalchemy.sql import and_, asc, desc, or_
from urllib.parse import urlparse
import os
import sys
import hashlib

a=".obenj".encode("UTF-8")
b=".obenj".encode("UTF-8")
c="atqofficial_".encode("UTF-8")
print(hashlib.md5(a).hexdigest())
print(hashlib.md5(b).hexdigest())
print(hashlib.md5(c).hexdigest())

tt_base64_file='_ericamarta-video-6928510470575885574_base64.txt'
tt_cover=model.TT_Cover()
print(tt_base64_file[:-37])
tt_cover.file_name=tt_base64_file[:-11]
tt_cover.user_id=hashlib.md5(tt_base64_file[:-37].encode('UTF-8')).hexdigest()
print(tt_cover.file_name)
print(tt_cover.user_id)

a="_ER175USP6M_base64.txt"
print(a[:-11])

# e0ed881daf501a95cecc241811fe990f

#
# # tmd图片怎么又tm和数据库差了一条 20220421
# def get_allfile(path):  # 获取所有文件
#     all_file = []
#     for f in os.listdir(path):  # listdir返回文件中所有目录
#         f_name = os.path.join('./screenshots/', f)
#         all_file.append(f_name)
#     return all_file
#
#
# sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
# engine = create_engine(sqlconn, echo=True, max_overflow=8)
# DBSession = sessionmaker(bind=engine)
# session = DBSession()
# rows = session.query(model.Site).filter(model.Site.type == 0).all()
# files = get_allfile('./screenshots/common/')
# # print(files[:])
# for row in rows:
#     if row.screenshot in files:
#         files.remove(row.screenshot)
# print(files[:])                         # id:24753   24753_0.png
# session.close()


#
# a = """333 Sex.Uno If you would like to support my channel, I will be very grateful, every donation is important to me 😚 https://www.paypal.com/donate/?hosted_button_id=8V8QP43EHZ3M8"""
# res = re.findall(r'((?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})+(?:(?:\/[=\w\?]+)*))+', a)
# print(res[:])
#
# a="https://quickdates0.com/?a=929626&cr=30815&lid=16559&mh=V1JVanNCR2prSVhrenNqT3dmQXd5T055eUJs"
# res = re.findall(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', a)
# print(res[:])

# def get_allfile(path):  # 获取所有文件
#     all_file = []
#     for f in os.listdir(path):  # listdir返回文件中所有目录
#         f_name = os.path.join(path, f)
#         all_file.append(f_name)
#     print('files: ', len(all_file))
#     return all_file
#
#
# sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
# engine = create_engine(sqlconn, echo=True, max_overflow=8)
# DBSession = sessionmaker(bind=engine)
# session = DBSession()
# rows = session.query(model.Site).filter(model.Site.type == 0).all()
# files = get_allfile('./screenshots/common/')
# print(files[:])
# for row in rows:
#     a = row.screenshot
#     a = a.replace('./screenshots/', './screenshots/common/')
#     if a in files:
#         files.remove(a)
#
# print('rows: ',len(rows))
# print(files[:])
# session.close()

# sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
# engine = create_engine(sqlconn, echo=True, max_overflow=8)
# DBSession = sessionmaker(bind=engine)
# session = DBSession()
# res = session.query(model.Site).filter(model.Site.type == 2, or_(model.Site.page_title.like('%dating%'),
#                                                                  model.Site.page_title.like('%交友%'))).all()
# print(len(res))
# session.close()

#
# # tmd图片怎么和数据库差了一条草了
# def get_allfile(path):  # 获取所有文件
#     all_file = []
#     for f in os.listdir(path):  # listdir返回文件中所有目录
#         f_name = os.path.join(path, f)
#         all_file.append(f_name)
#     return all_file
#
#
# sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
# engine = create_engine(sqlconn, echo=True, max_overflow=8)
# DBSession = sessionmaker(bind=engine)
# session = DBSession()
# rows = session.query(model.Site).filter(model.Site.type == 2).all()
# files = get_allfile('./screenshots/')
# print(files[:])
# for row in rows:
#     if row.screenshot in files:
#         files.remove(row.screenshot)
# print(files[:])                         # tmd找到了 id:20568   20568_0.png
# session.close()


# a = re.findall(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', "_KUYYA.SITE.eeee.oi")
# print(a)

#
# browser = webdriver.Chrome()
# try:
#     browser.get('http://i.want.you')
#     time.sleep(5)
#     # 获取网站的信息
#     http_status = '响应成功'
#     if browser.title:
#         title = browser.title
#         print(title)
#     else:
#         title = ''
#     print('响应成功')
# except:
#     print('响应失败')

# str = '''*Son unos de los **babes.Camsoda.Uno*    mañas no se la  Sun: 'Hotter'  Sugar: 'Sweeter'  Joonie: 'Cooler'  Yoongi: 'Butter'    Son unos de los mejores conciertos  , no puede ir pero de tan solo verlos desde pantalla, se que estuvo sorprendente,'''

# url="baidu.com"
#
# a=re.findall(r'(?:[\w](?:[\w\-]{0,61}[\w])?\.)+[a-zA-Z]{2,6}',url)
# print(a)

# a="http://www.youtube.com/channel/UCj5LuOzJgPOe8F-WH0Hbmrw"
# print(a[-24:])
#
# a = "234,567位订阅者"
# a = ''.join(filter(str.isdigit, a))
#
# print(a)
#
# index = {
#     "VideoID": 0, "PublishedAt": 1, "ChannelId": 2, "CategoryID": 3, "Title": 4, "Description": 5, "ChannelTitle": 6,
#     "LiveBroadcastContent": 7, "Duration": 8, "Dimension": 9, "Definition": 10, "Caption": 11, "LicensedContent": 12,
#     "ViewCount": 13, "LikeCount": 14, "DislikeCount": 15, "FavoriteCount": 16, "CommentCount": 17, "PrivacyStatus": 18,
#     "License": 19, "Embeddable": 20, "PublicStatsViewable": 21, "TopicIds": 22, "RelevantTopicIds": 23
# }
#
# str_test = "pKCRz-hta_A	2022-03-18T12:14:25Z	UCbd0IJ1OJAVcjjEH4t9VjEw	22	Wow😱🔥 #shorts		KYLIE-LUNA	none	PT23S	2d	hd	false	false	46409	1169		0	33	public	youtube	true	true		"
# str_test = str_test.split("\t")
# # print(str_test[:])
# for key, value in index.items():
#      print("{0}: {1}".format(key, str_test[value]))

# publisher_link = 'https://www.tiktok.com/tag/wearitbigchallenge'
# browser = webdriver.Chrome()
#
# browser.get(publisher_link)
# time.sleep(4)
#
# item = browser.find_element_by_css_selector('div.tiktok-yz6ijl-DivWrapper')
# html = item.get_attribute('innerHTML')
# # print(html)
# html = etree.HTML(html)
# video_link = html.cssselect('a')[0].attrib['href']
# img_name = re.sub('\/', '-', video_link[24:])
# print(img_name)
#
# img_link = html.cssselect('img')[0].attrib['src']
# img_link = 'http' + img_link[5:]
# print(img_link)
#
# browser.close()

# a = '43,567'
# a = re.sub('(,)', '', a)
# print(a)
#
# a = 'https://www.youtube.com/shorts/AUXSZtyAnGk'
# print(a[-11:])
#
# a='https://p16-sign-va.tiktokcdn.com/obj/tos-maliva-p-0068/48db56c1a76c49caae0252d81c6a67be_1625801686?x-expires=1648562400&x-signature=BG6M3kRCvDGv4ocEsZwG%2FPZHIIc%3D'
#
# print(a[5:])
#
# # 将获取到的图片二进制流写入本地文件
# with open('xxx.jpg', 'wb') as f:
#     # 通过requests发送一个get请求到图片地址，返回的响应就是图片内容
#     r = requests.get('http://i.ytimg.com/vi/eSvIOXueP5U/hq2.jpg')   # 注意不能https
#     f.write(r.content)
#
# URL = 'http://i.ytimg.com/vi/eSvIOXueP5U/hq.jpg'
# try:
#     r = requests.get(URL, timeout=1)
#     r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
# except requests.RequestException as e:
#     print(e)
# else:
#     result = r.content
#     print(type(result), result, sep='\n')

# try:
#     r = requests.get('http://p16-sign-va.tiktokcdn.com/obj/tos-maliva-p-0068/48db56c1a76c49caae0252d81c6a67be_1625801686?x-expires=1648562400&x-signature=BG6M3kRCvDGv4ocEsZwG%2FPZHIIc%3D', timeout=2)
#     r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
# except requests.RequestException as e:
#     print(e)
# else:
#     with open('ttt.jpg', 'wb') as f:
#         f.write(r.content)
