from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql

Base = declarative_base()


# 定义对象
class Video(Base):
    # 表名
    __tablename__ = 'video'

    id = Column(mysql.BIGINT, primary_key=True)
    title = Column(String(100))
    video_id = Column(String(24))
    publisher = Column(String(64))
    publisher_link = Column(String(256))
    video_link = Column(String(256))
    date = Column(String(20))
    views = Column(Integer)
    description = Column(String(4096))
    comments_count = Column(Integer)


class Comment(Base):
    # 表名
    __tablename__ = 'comment'

    id = Column(mysql.BIGINT, primary_key=True)
    video_id = Column(String(24))
    user = Column(String(64))
    user_link = Column(String(256))
    content = Column(String(2048))
    date = Column(String(20))


class User(Base):
    # 表名
    __tablename__ = 'user'

    id = Column(mysql.BIGINT, primary_key=True)
    type = Column(SmallInteger)
    username = Column(String(64))
    homepage = Column(String(256))
    subscribers = Column(String(10))
    views = Column(Integer)
    join_time = Column(String(30))
    description = Column(String(4096))
    details = Column(String(1024))
    links = Column(String(4096))
    user_id = Column(String(24))


class Site(Base):
    # 表名
    __tablename__ = 'site'

    id = Column(mysql.BIGINT, primary_key=True)
    comment_id = Column(mysql.BIGINT)
    user_id = Column(String(24))
    url = Column(String(256))
    land_page = Column(String(2048))
    page_title = Column(String(256))
    screenshot = Column(String(256))
    type = Column(SmallInteger)
