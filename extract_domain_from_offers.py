from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy.sql import and_, asc, desc, or_
from model import Affpay_Offer, Odigger_Offer, Offervault_Offer
import os
import re
import requests

sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
proxy = '127.0.0.1:1080'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
}

if __name__ == '__main__':
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # affpay
    rows = session.query(Affpay_Offer).all()
    domain_list = []
    for row in rows:
        if row.land_page and '/' in row.land_page:
            print(row.land_page)
            domain = row.land_page.split("/")[2]
            if domain in domain_list:
                continue
            else:
                domain_list.append(domain)
    for domain in domain_list:
        f = open('./url_in_offers.txt', 'a', encoding='UTF8')
        f.write(domain + '\n')
        f.close()

    # offervault
    rows = session.query(Offervault_Offer).all()
    domain_list = []
    for row in rows:
        if row.land_page and '/' in row.land_page:
            domain = row.land_page.split("/")[2]
            if domain in domain_list:
                continue
            else:
                domain_list.append(domain)
    for domain in domain_list:
        f = open('./url_in_offers.txt', 'a', encoding='UTF8')
        f.write(domain + '\n')
        f.close()

    # odigger
    rows = session.query(Odigger_Offer).all()
    domain_list = []
    for row in rows:
        if row.land_page and '/' in row.land_page:
            domain = row.land_page.split("/")[2]
            if domain in domain_list:
                continue
            else:
                domain_list.append(domain)
    for domain in domain_list:
        f = open('./url_in_offers.txt', 'a', encoding='UTF8')
        f.write(domain + '\n')
        f.close()

    session.close()
