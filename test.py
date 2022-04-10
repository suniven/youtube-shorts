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
from urllib.parse import urlparse

url = '''*Son unos de los **babes.Camsoda.Uno*    mañas no se la  Sun: 'Hotter'  Sugar: 'Sweeter'  Joonie: 'Cooler'  Yoongi: 'Butter'    Son unos de los mejores conciertos  , no puede ir pero de tan solo verlos desde pantalla, se que estuvo sorprendente,'''

parse = urlparse(url)

print(parse)

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
