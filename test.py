from selenium.webdriver.common.keys import Keys

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
from timestamp import timestamp_datetime
import base64

a = {
    0: 2,
    3: 1,
    4: 9
}
print(1+ (0 in a))

# print('.'.join("baefidd.bustyaffar.com".split('.')[-2:]))


#
# def control_in_shadow(browser, js):
#     item = browser.execute_script(js)
#     # print(type(item))
#     return item  # 返回的对象在这里
#
#
# def scroll(browser):
#     browser.execute_script('window.scrollBy(0,500)')
#
#
# def find_subdomain(browser, js):
#     item = browser.execute_script(js)
#     if item:
#         return True
#     print("NO")
#     return False
#
#
# def load_more_subdomain(browser):
#     try:
#         # # 取消隐藏
#         # js_remove_hidden = 'document.getElementsByTagName("domain-view")[0].shadowRoot.getElementById("relations").shadowRoot.querySelector("vt-ui-button").removeAttribute("hidden")'
#         # browser.execute_script(js_remove_hidden)
#         while True:
#             print("loading...")
#             js_load_btn = 'document.getElementsByTagName("domain-view")[0].shadowRoot.getElementById("relations").shadowRoot.querySelector(".subdomains").querySelector(".load-more").click()'
#             browser.execute_script(js_load_btn)
#             time.sleep(2)
#
#             js_trs = 'return document.getElementsByTagName("domain-view")[0].shadowRoot.getElementById("relations").shadowRoot.querySelector(".subdomains").querySelector("vt-ui-generic-list").shadowRoot.querySelectorAll(".tr")'
#             trs = control_in_shadow(browser, js_trs)
#             print(len(trs))
#     except Exception as err:
#         print(err)
#         return

#
# if __name__ == '__main__':
#     # browser = webdriver.Chrome()
#     # browser.maximize_window()
#     # url = 'https://www.virustotal.com/gui/domain/womenscutest.life/relations'
#     # browser.get(url)
#     # time.sleep(2)
#     # load_more_subdomain(browser)
#     # js_trs = 'return document.getElementsByTagName("domain-view")[0].shadowRoot.getElementById("relations").shadowRoot.querySelector("vt-ui-generic-list").shadowRoot.querySelectorAll(".tr")'
#     # trs = control_in_shadow(browser, js_trs)
#     # print(len(trs))
#     # time.sleep(5)
#     #
#     sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
#     engine = create_engine(sqlconn, echo=True, max_overflow=8)
#     DBSession = sessionmaker(bind=engine)
#     session = DBSession()
#     rows = session.query(model.Virustotal_Subdomain).filter().all()
#     print(len(rows))
#     # browser.quit()

#
# def control_in_shadow(browser, js):
#     item = browser.execute_script(js)
#     print(type(item))
#     return item  # 返回的对象在这里
#
#
# browser = webdriver.Chrome()
# browser.maximize_window()
# virustotal_url_page = 'https://www.virustotal.com/gui/url/b77fba6dce9cb493a319e2dcf81e018d99ec14438fcbf2410738fc9eb58c0246'
# browser.get(virustotal_url_page)
# time.sleep(2)
# js_numerator = 'return document.getElementsByTagName("url-view")[0].shadowRoot.getElementById("report").shadowRoot.querySelector(".veredict-widget vt-ui-detections-widget").shadowRoot.querySelector(".positives")'
# numerator = control_in_shadow(browser, js_numerator).text
# print(numerator)
# js_detections = 'return document.getElementsByTagName("url-view")[0].shadowRoot.querySelector("vt-ui-detections-list").shadowRoot.querySelector("#detections")'
# detections = control_in_shadow(browser, js_detections)
# detection_list = detections.find_elements_by_css_selector('.detection')
# print(type(detection_list))
# print(len(detection_list))
# for detection in detection_list:
#     vendor = detection.find_element_by_css_selector('.engine-name').text
#     analysis = detection.find_element_by_css_selector('.individual-detection').text
#     print("{0}: {1}".format(vendor, analysis))
#
# js_detail = 'return document.getElementsByTagName("url-view")[0].shadowRoot.getElementById("report").shadowRoot.querySelectorAll("vt-ui-button")[2]'
# detail_btn = control_in_shadow(browser, js_detail)
# detail_btn.click()
#
# js_cate = 'return document.getElementsByTagName("url-view")[0].shadowRoot.getElementById("details").shadowRoot.querySelector("vt-ui-expandable span vt-ui-key-val-table").shadowRoot.querySelectorAll(".row")'
# cate_list = control_in_shadow(browser, js_cate)
# for cate in cate_list:
#     engine = cate.find_element_by_css_selector('.label').text
#     category = cate.find_element_by_css_selector('.value').text
#     print("{0}: {1}".format(engine, category))
#
# time.sleep(5)
# browser.quit()

# f1 = open("./txt files/temp1.txt", "r", encoding="UTF8")
# f2 = open("./txt files/temp2.txt", "w", encoding="UTF8")
# f3 = open("./txt files/url_in_comments.txt", "r", encoding="UTF8")
#
# done_list = f1.readlines()
# c_list = f3.readlines()
# for i in range(len(done_list)):
#     done_list[i] = done_list[i].strip('\n')
# for i in range(len(c_list)):
#     c_list[i] = c_list[i].strip('\n')
#
# for done in done_list:
#     if done in c_list:
#         c_list.remove(done)
#
# print("len: ", len(c_list))
# print(c_list[:])
# for item in c_list:
#     f2.write(item + '\n')
#
# f1.close()
# f2.close()
# f3.close()

# import ssl
# from googlesearch import search, get_random_user_agent
#
# ssl._create_default_https_context = ssl._create_unverified_context
# for url in search('"Brisex.Uno"', stop=20, user_agent=get_random_user_agent()):  # stop=None
#     print(url)
#
# def test(a=9):
#     print(a)
#
#
# test(a=10)

# curl 'https://customsearch.googleapis.com/customsearch/v1?cx=a7dbc3e35111d44eb&num=20&q=%22BRISEX.Uno%22&access_token=AIzaSyD7MID4GdYQt3YKUqsqIlKZiPxtU-NPNnM&key=AIzaSyD7MID4GdYQt3YKUqsqIlKZiPxtU-NPNnM' --header 'Accept: application/json' --compressed

#
# '''
# 通用文字识别
# '''
#
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
# params = {
#     "url": "https://www.whois.com/eimg/5/07/507f3d6c2ced8585e10f84abc754f3c10ae1c619.png",
#     "language_type": "ENG"
# }
# access_token = '24.0517a9b8c406efc450556ac5df9a0880.2592000.1655785788.282335-26288350'
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/x-www-form-urlencoded'}
# response = requests.post(request_url, data=params, headers=headers)
# if response:
#     print(response.json())

# print(timestamp_datetime(1652809740))
# print(timestamp_datetime(time.time()))

#
# a = 'https://www.paypal.com/donate/?hosted_button_id=8V8QP43EHZ3M8'
# print(a.split('/')[2])
#
# sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
# engine = create_engine(sqlconn, echo=True, max_overflow=8)
# DBSession = sessionmaker(bind=engine)
# session = DBSession()
# rows = session.query(model.Affpay_Offer).all()
# print(len(rows))

# page = re.findall(r'page=[0-9]+', 'https://offervault.com/?selectedTab=topOffers&search=&page=199')[0][5:]
# print(page)

# browser = webdriver.Chrome()
# browser.get("https://www.datingleben.com/mlp9/")
# time.sleep(2)
# url = browser.current_url
# print("url： ", url)
# browser.close()
# browser.quit()

# browser.get("https://www.sina.com")
# time.sleep(4)
# browser.get("https://www.bing.com")
# time.sleep(4)
# browser.close()
# print("close")          # close的是handle  get是在当前handle

#
# def findTheWinner(n: int, k: int) -> int:
#     nums = [i + 1 for i in range(n)]
#     cur_index = 0
#     cur_num = n
#     while len(nums) != 1:
#         # print(nums[:])
#         cur_index = (cur_index + k - 1) % cur_num
#         nums.pop(cur_index)
#         cur_num = cur_num - 1
#         cur_index = cur_index % cur_num
#     return nums[0]
#
#
# x = findTheWinner(5, 2)
# print(x)

# a = ".obenj".encode("UTF-8")
# b = ".obenj".encode("UTF-8")
# c = "atqofficial_".encode("UTF-8")
# print(hashlib.md5(a).hexdigest())
# print(hashlib.md5(b).hexdigest())
# print(hashlib.md5(c).hexdigest())
#
# tt_base64_file = '_ericamarta-video-6928510470575885574_base64.txt'
# tt_cover = model.TT_Cover()
# print(tt_base64_file[:-37])
# tt_cover.file_name = tt_base64_file[:-11]
# tt_cover.user_id = hashlib.md5(tt_base64_file[:-37].encode('UTF-8')).hexdigest()
# print(tt_cover.file_name)
# print(tt_cover.user_id)
#
# a = "_ER175USP6M_base64.txt"
# print(a[:-11])

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
