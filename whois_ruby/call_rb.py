import os
import time
import re
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy.sql import and_, asc, desc, or_
from timestamp import get_now_timestamp
from model import Domain

sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'


def call_ruby_script(domain_name):
    cmd = 'get_domain_info.rb -d ' + domain_name
    result = os.popen(cmd)
    # print(result.read())
    if "ServerNotFound" in result:
        print("No Domain Info.")
        return
    result = result.read()
    domain_info = Domain()
    domain_info.domain_name = domain_name
    domain_info.raw_data = result
    domain_info.registrant_id = ''
    domain_info.registrant_name = ''
    domain_info.registrant_organization = ''
    domain_info.registrant_street = ''
    domain_info.registrant_city = ''
    domain_info.registrant_province = ''
    domain_info.registrant_postal_code = ''
    domain_info.registrant_country = ''
    domain_info.registrant_phone = ''
    domain_info.registrant_phone_ext = ''
    domain_info.registrant_fax = ''
    domain_info.registrant_fax_ext = ''
    domain_info.registrant_email = ''

    lines = result.splitlines()
    for line in lines:
        if "Registrant" in line:
            items = line.split(':')
            if items[0] == 'Registry Registrant ID':
                if items[1]:
                    domain_info.registrant_id = items[1]
            elif items[0] == 'Registrant Name':
                if items[1]:
                    domain_info.registrant_name = items[1]
            elif items[0] == 'Registrant Organization':
                if items[1]:
                    domain_info.registrant_organization = items[1]
            elif items[0] == 'Registrant Street':
                if items[1]:
                    domain_info.registrant_street = items[1]
            elif items[0] == 'Registrant City':
                if items[1]:
                    domain_info.registrant_city = items[1]
            elif items[0] == 'Registrant State/Province':
                if items[1]:
                    domain_info.registrant_province = items[1]
            elif items[0] == 'Registrant Postal Code':
                if items[1]:
                    domain_info.registrant_postal_code = items[1]
            elif items[0] == 'Registrant Country':
                if items[1]:
                    domain_info.registrant_country = items[1]
            elif items[0] == 'Registrant Phone':
                if items[1]:
                    domain_info.registrant_phone = items[1]
            elif items[0] == 'Registrant Phone Ext':
                if items[1]:
                    domain_info.registrant_phone_ext = items[1]
            elif items[0] == 'Registrant Fax':
                if items[1]:
                    domain_info.registrant_fax = items[1]
            elif items[0] == 'Registrant Fax Ext':
                if items[1]:
                    domain_info.registrant_fax_ext = items[1]
            elif items[0] == 'Registrant Email':
                if items[1]:
                    domain_info.registrant_email = items[1]

    session.add(domain_info)
    session.commit()


if __name__ == '__main__':
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    f = open("../txt files/domain_in_comments.txt", "r", encoding="UTF8")
    # f = open("../txt files/domain_in_offers.txt", "r", encoding="UTF8")
    domain_list = f.readlines()
    f.close()

    for domain in domain_list:
        domain = domain.strip('\n')
        if domain:
            domain = domain.split('.')[-2:]
            rows = session.query(Domain).filter(Domain.domain_name.like(domain_name)).all()
            if rows:
                continue
            call_ruby_script(domain)

    session.close()
