# 根据site的type对对应的comment打标签

from timestamp import get_now_timestamp
from sqlalchemy.sql import and_, asc, desc, or_
from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy import text
from model import Comment, Site

sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'

if __name__ == '__main__':
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    sites = session.query(Site).filter(Site.type == 1).all()
    for site in sites:
        cid = site.comment_id
        res = session.query(Comment).filter(Comment.id == cid).update({"type": 1})
        session.commit()

    session.close()
