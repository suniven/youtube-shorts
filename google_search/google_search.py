import os
import time
import requests
import json
from model import Google_Search_Result
from timestamp import get_now_timestamp
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy.sql import and_, asc, desc, or_

# GET https://customsearch.googleapis.com/customsearch/v1?cx=[cx]&q=[query]&key=[API-Key] HTTP/1.1
#
# Accept: application/json

proxy = '127.0.0.1:1080'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
}
sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'


def send_request(query, session):
    request_url = "https://customsearch.googleapis.com/customsearch/v1"
    cx = 'a7dbc3e35111d44eb'
    key = 'AIzaSyD7MID4GdYQt3YKUqsqIlKZiPxtU-NPNnM'
    request_url = request_url + "?cx=" + cx + "&q=" + query + "&key=" + key
    headers = {'content-type': 'application/json'}
    response = requests.get(request_url, headers=headers, proxies=proxies)
    if response:
        # print(response.json())
        data = response.json()
        try:
            items = data["items"]
            for item in items:
                google_search_result = Google_Search_Result()
                google_search_result.query = query.replace("\"", "")
                google_search_result.title = item["title"]
                google_search_result.url = item["link"]
                google_search_result.snippet = item["snippet"]
                google_search_result.create_time = get_now_timestamp()
                session.add(google_search_result)
                session.commit()
        except Exception as err_msg:
            print("** ", err_msg)
            f_err = open("./error_log.txt", "a", encoding="UTF8")
            f_err.write("Error: Query {0}\tErrMsg: {1}\n".format(query, err_msg))
            f_err.close()


if __name__ == '__main__':
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    f = open("../txt files/domain_in_comments.txt", "r", encoding="UTF8")
    # f = open("../txt files/for_test.txt", "r", encoding="UTF8")
    domain_list = f.readlines()
    f.close()
    for domain in domain_list:
        domain = domain.strip('\n')
        if domain:
            domain = '.'.join(domain.split('.')[-2:])
            kw = "\"" + domain + "\""
            print("-- Query: {0} --".format(kw))
            send_request(kw, session)
            time.sleep(8)
    session.close()
