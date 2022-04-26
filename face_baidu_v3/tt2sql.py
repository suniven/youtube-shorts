from model import TT_Cover
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
import hashlib
import os

if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4', echo=True,
                           max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    tt_base64_path = '../cover_img/tt_base64/'
    tt_base64_list = os.listdir(tt_base64_path)
    tt_base64_list.remove('no face')

    for tt_base64_file in tt_base64_list:
        tt_cover = TT_Cover()
        tt_cover.file_name = tt_base64_file[:-11]
        tt_cover.user_id = hashlib.md5(tt_base64_file[:-37].encode('UTF-8')).hexdigest()
        # print("Insert {0}...\nUserId: {1}".format(tt_cover.file_name, tt_cover.user_id))
        session.add(tt_cover)
        session.commit()
    session.close()
