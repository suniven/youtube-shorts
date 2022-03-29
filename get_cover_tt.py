import model
import time
import re
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql



if __name__ == '__main__':
    publisher_link = ''
    browser = webdriver.Chrome()
    try:
        browser.get(publisher_link)
        time.sleep(4)


    finally:
        browser.close()
