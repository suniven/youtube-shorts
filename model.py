from sqlalchemy import Column, String, create_engine, Integer
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
    publisher = Column(String(64))
    publisher_link = Column(String(1024))
    video_link = Column(String(1024))
    date = Column(String(20))
    views = Column(Integer)


class Comment:
    def __init__(self):
        self.id = 0
        self.vid = 0
        self.user = ''
        self.user_link = ''
        self.content = ''


class User:
    def __init__(self):
        self.id = 0
        self.type = 0
        self.username = ''
        self.homepage = ''
        self.subscribers = ''
        self.views = 0
        self.join_time = ''
        self.description = ''
        self.details = ''
        self.links = ''
