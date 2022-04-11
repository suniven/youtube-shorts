# 计划先按照关键词如uno打标签
# 剩下的根据截图，写个辅助工具人工打标签

from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy import text
from model import Site, Comment
import os
import sys
import shutil

porn_keywords = ['.uno', '.baby', '.site']
common_keywords = ['.fo', '.tokyo', 'youtu.be', '.sv', 'paypal', 'youtube.com']  # 不过.tokyo个人感觉还是挺奇怪的

sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'

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