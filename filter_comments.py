# TODO: 统计评论中包含色情链接的数量
# TODO: 将包含色情链接的评论打上tag
# TODO: 将发布此类评论的用户打上tag并统计每名用户发了多少条此类评论
# TODO: 访问色情链接，保存跳转后的落地页链接

from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy import text
from model import Comment
import re

if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:1101syw@localhost:3306/youtube_shorts?charset=utf8mb4', echo=True,
                           max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    comments = session.query(Comment).filter(
        Comment.content.op('regexp')(r'([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}')).all()
    session.close()

    print("len: ",len(comments))
    for comment in comments:
        # print(comment)
        link = re.findall(r'(?:[\w](?:[\w\-]{0,61}[\w])?\.)+[a-zA-Z]{2,6}', comment.content)
        print(comment.id, comment.user_link[-12:], link)
