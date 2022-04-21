from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy import text
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import re
import os
import requests
import time

sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/test?charset=utf8mb4'
path = './domain_info'

if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=option)

    f = open("./domain_info/land_page_domain.txt", encoding='UTF-8')
    domains = f.readlines()
    for domain in domains:
        domain = domain.strip('\n')
        file_path = "./domain_info/" + domain + ".txt"
        # f_domain = open(file_path, "r", encoding="UTF-8")
        # content = f_domain.read()
        # if content:
        #     print("{0} already exist.".format(domain))
        #     f_domain.close()
        #     continue
        try:
            f_domain = open(file_path, "w+", encoding="UTF-8")
            print("-----------------------------")
            print("Getting info of {0} ...".format(domain))
            url = "https://www.whois.com/whois/" + domain
            browser.get(url)
            raw_data = browser.find_element_by_css_selector(
                '#page-wrapper > div > div.main-col > div.whois-data > div.df-block-raw').get_attribute('innerHTML')
            f_domain.write(raw_data)
            print("Writing info of {0} ...".format(domain))
            print("-----------------------------")
            f_domain.close()
        except Exception as e:
            print("Error: ", e)
        time.sleep(5)
    f.close()
    browser.quit()
