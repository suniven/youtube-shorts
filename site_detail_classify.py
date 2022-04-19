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

    rows = session.query(Site).filter(Site.land_page.like('%https://www.be.to/%')).all()

    for row in rows:
        try:
            # shutil.move(row.screenshot, "./screenshots/common/")
            # print("{0} has been moved.".format(row.screenshot))
            row.detail = "邮箱广告"
            session.commit()
        except Exception as e:
            print("Err: ", e)
    session.close()