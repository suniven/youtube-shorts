# 计划先按照关键词如uno打标签
# 剩下的根据截图，写个辅助工具人工打标签

from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy import text
from sqlalchemy.sql import and_, asc, desc, or_
from model import Site, Comment
import os
import sys
import shutil

if __name__ == '__main__':
    sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test-0414?charset=utf8mb4'
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    rows = session.query(Site).filter(Site.url.like('%IN.SV/REDPUSSY%')).all()

    for row in rows:
        try:
            # shutil.move(row.screenshot, "./screenshots/common/")
            # print("{0} has been moved.".format(row.screenshot))
            row.type = 1
            session.commit()
        except Exception as e:
            print("Err: ", e)
    session.close()

"""
if __name__ == '__main__':
    sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    rows = session.query(Site).filter(Site.type == 1).all()
    for row in rows:
        id = row.comment_id
        res = session.query(Comment).filter(Comment.id == id).update({"type": 1})
        session.commit()

    session.close()
"""
"""
if __name__ == '__main__':
    sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test-0414?charset=utf8mb4'
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # 给普通网站打标签 + 给图片分类
    # synchronize_session=False *****
    # common_keywords = ['youtu.be', '.sv', 'paypal', 'youtube.com']
    rows = session.query(Site).filter(Site.type == 2, or_(Site.url.like('%youtu.be%'),
                                                          Site.url.like('%.sv%'),
                                                          Site.url.like('%youtube.com%'),
                                                          Site.url.like('%paypal%'))).all()

    for row in rows:
        try:
            shutil.move(row.screenshot, "./screenshots/common")
            print("{0} has been moved.".format(row.screenshot))
            row.type = 0
            session.commit()
        except Exception as e:
            print("Err: ", e)
    session.close()
"""

"""
if __name__ == '__main__':
    # 根据page_title的关键词
    sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test-0414?charset=utf8mb4'
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # 给色情网站打标签 + 给图片分类
    # synchronize_session=False *****
    # rows = session.query(Site).filter(Site.type == 2, or_(Site.page_title.like('%dating%'),
    #                                                       Site.page_title.like('%交友%'))).all()

    # rows = session.query(Site).filter(Site.type == 2, or_(Site.url.like('%.uno%'),
    #                                                       Site.url.like('%.tokyo%'),
    #                                                       Site.url.like('%.site%'),
    #                                                       Site.url.like('%.baby%'))).all()

    # rows = session.query(Site).filter(Site.type == 2, or_(Site.page_title.like('%verification%'),
    #                                                       Site.page_title.like('%sexy%'),
    #                                                       Site.page_title.like('%laid%'),
    #                                                       Site.page_title.like('%olivia%'))).all()

    rows = session.query(Site).filter(Site.type == 2, or_(Site.url.like('%.online%'),
                                                          Site.url.like('%VUM.TODAY%'),
                                                          Site.url.like('%IN.SV%'))).all()

    for row in rows:
        try:
            shutil.move(row.screenshot, "./screenshots/porn/")
            print("{0} has been moved.".format(row.screenshot))
            row.type = 1
            session.commit()
        except Exception as e:
            print("----------")
            print("Err: ", e)
            print("----------")
    session.close()
"""

"""
# 根据url的关键词

porn_keywords = ['.uno', '.baby', '.site', '.tokyo', '.fo']
common_keywords = ['youtu.be', '.sv', 'paypal', 'youtube.com']

sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test-0414?charset=utf8mb4'

if __name__ == '__main__':
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # 给色情网站打标签 + 给图片分类
    # synchronize_session=False *****
    for keyword in porn_keywords:
        res = session.query(Site).filter(Site.url.like('%' + keyword + '%')).update({"type": 1},
                                                                                    synchronize_session=False)
        session.commit()
        print('{0}: Update {1} rows.'.format(keyword, res))

    # 给普通网站打标签 + 给图片分类
    for keyword in common_keywords:
        res = session.query(Site).filter(Site.url.like('%' + keyword + '%')).update({"type": 0},
                                                                                    synchronize_session=False)
        session.commit()
        print('{0}: Update {1} rows.'.format(keyword, res))

    rows = session.query(Site).filter(Site.type==0).all()
    for row in rows:
        try:
            shutil.move(row.screenshot, "./screenshots/common/")
            print("{0} has been moved.".format(row.screenshot))
        except:
            print("{0} has already been moved.".format(row.screenshot))

    rows = session.query(Site).filter(Site.type == 1).all()
    for row in rows:
        try:
            shutil.move(row.screenshot, "./screenshots/porn/")
            print("{0} has been moved.".format(row.screenshot))
        except:
            print("{0} has already been moved.".format(row.screenshot))

    session.close()
"""
