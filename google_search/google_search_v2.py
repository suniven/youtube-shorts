# 调用googlesearch module
# 返回更多结果

import time
import requests
import json
from model import Google_Search_Result
from timestamp import get_now_timestamp
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from model import Google_Search_Result
from googlesearch import search, get_random_user_agent
import ssl

# ssl._create_default_https_context = ssl._create_unverified_context
sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
proxy = '127.0.0.1:1080'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
}


def send_request(query, session):
    for url in search(query, stop=20, verify_ssl=True, user_agent=get_random_user_agent()):  # stop=None
        google_search_result = Google_Search_Result()
        google_search_result.query = query.replace("\"", "")
        google_search_result.title = ""
        google_search_result.url = url
        google_search_result.snippet = ""
        google_search_result.create_time = get_now_timestamp()
        session.add(google_search_result)
        session.commit()


if __name__ == '__main__':
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    f = open("../txt files/url_in_comments.txt", "r", encoding="UTF8")
    # f = open("../txt files/for_test.txt", "r", encoding="UTF8")
    url_list = f.readlines()
    f.close()
    for url in url_list:
        url = url.strip('\n')
        if url:
            kw = "\"" + url + "\""
            print("-- Query: {0} --".format(kw))
            rows = session.query(Google_Search_Result).filter(Google_Search_Result.query.like(kw)).all()
            if rows:
                continue
            send_request(kw, session)
            time.sleep(8)
    session.close()
