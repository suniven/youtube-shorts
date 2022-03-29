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

publisher_link = 'https://www.tiktok.com/tag/wearitbigchallenge'
browser = webdriver.Chrome()

browser.get(publisher_link)
time.sleep(4)

item = browser.find_element_by_css_selector('div.tiktok-yz6ijl-DivWrapper')
html = item.get_attribute('innerHTML')
# print(html)
html = etree.HTML(html)
video_link = html.cssselect('a')[0].attrib['href']
img_name = re.sub('\/', '-', video_link[24:])
print(img_name)

img_link = html.cssselect('img')[0].attrib['src']
img_link = 'http' + img_link[5:]
print(img_link)

browser.close()

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
