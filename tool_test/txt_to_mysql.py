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

video_index = {
    "VideoID": 0, "PublishedAt": 1, "ChannelId": 2, "CategoryID": 3, "Title": 4, "Description": 5, "ChannelTitle": 6,
    "LiveBroadcastContent": 7, "Duration": 8, "Dimension": 9, "Definition": 10, "Caption": 11, "LicensedContent": 12,
    "ViewCount": 13, "LikeCount": 14, "DislikeCount": 15, "FavoriteCount": 16, "CommentCount": 17, "PrivacyStatus": 18,
    "License": 19, "Embeddable": 20, "PublicStatsViewable": 21, "TopicIds": 22, "RelevantTopicIds": 23
}

comment_index = {
    "Blank": 0, "Blank": 1, "VideoID": 2, "CommentID": 3, "CommentPublished": 4, "CommentUpdated": 5,
    "CommentTextDisplay": 6, "CommentAuthorName": 7, "CommentAuthorURI": 8, "CommentCanReply": 9,
    "CommentTotalReplyCount": 10, "CommentisPublic": 11, "CommentLikeCount": 12, "CommentVewerRating": 13,
    "IsReply": 14, "CommentPosterInfo": 15
}

if __name__ == '__main__':
    # 评论
    f = open("./_comments/vid.comments.txt", encoding='UTF-8')  # 返回一个文件对象
    line = f.readline()
    i = 1
    engine = create_engine('mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4', echo=True,
                           max_overflow=8)

    while line:
        print("i: ", i)
        # print(line, end='')
        line = f.readline()
        line = line.split("\t")
        print('\n')
        # for key, value in video_index.items():
        #     print("{0}: {1}".format(key, line[value]))
        comment = model.Comment()
        comment.video_id = line[comment_index["VideoID"]]
        comment.user = line[comment_index["CommentAuthorName"]]
        comment.content = line[comment_index["CommentTextDisplay"]]
        comment.user_link = line[comment_index["CommentAuthorURI"]]
        comment.date = line[comment_index["CommentPublished"]]

        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        session.add(comment)
        session.commit()
        i = i + 1
        print("-----------------------")

    session.close()
    f.close()

    #
    # # 视频
    # f = open("./_video/vid_vidinfo.txt", encoding='UTF-8')  # 返回一个文件对象
    # line = f.readline()
    # i = 1
    # engine = create_engine('mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4', echo=True,
    #                        max_overflow=8)
    #
    # while line:
    #     print("i: ", i)
    #     # print(line, end='')
    #     line = f.readline()
    #     line = line.split("\t")
    #     print('\n')
    #     # for key, value in video_index.items():
    #     #     print("{0}: {1}".format(key, line[value]))
    #     video = model.Video()
    #     video.video_link = "https://www.youtube.com/watch?v=" + line[video_index["VideoID"]]
    #     video.video_id = line[video_index["VideoID"]]
    #     video.title = line[video_index["Title"]]
    #     video.views = int(line[video_index["ViewCount"]])
    #     video.date = line[video_index["PublishedAt"]]
    #     if line[video_index["CommentCount"]]:
    #         video.comments_count = int(line[video_index["CommentCount"]])
    #     else:
    #         video.comments_count = 0
    #     video.publisher_link = "https://www.youtube.com/channel/" + line[video_index["ChannelId"]] + "/videos"
    #     video.publisher = line[video_index["ChannelId"]]
    #     video.description = line[video_index["Description"]]
    #
    #     DBSession = sessionmaker(bind=engine)
    #     session = DBSession()
    #     session.add(video)
    #     session.commit()
    #     i = i + 1
    #     print("-----------------------")
    #
    # session.close()
    # f.close()

    # str_test = "pKCRz-hta_A	2022-03-18T12:14:25Z	UCbd0IJ1OJAVcjjEH4t9VjEw	22	Wow😱🔥 #shorts		KYLIE-LUNA	none	PT23S	2d	hd	false	false	46409	1169		0	33	public	youtube	true	true"

    # print(str_test[:])
