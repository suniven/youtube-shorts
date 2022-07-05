# not work.

import re
import time
import model
from timestamp import datetime_timestamp, timestamp_datetime, get_now_timestamp
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.maximize_window()
    try:
        browser.get('https://url-classification.io/test-a-site/')
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector('.form-input-text').send_keys('AisiU.Icu')

        iframe=browser.find_element_by_css_selector('#test-a-site > div.g-recaptcha > div > div > iframe')
        browser.switch_to.frame(iframe)
        reCAPTCHA = browser.find_element_by_css_selector('.recaptcha-checkbox-border').click()
        time.sleep(5)

        browser.switch_to.default_content()
        btn=browser.find_element_by_css_selector('.form-button').click()
        time.sleep(5)
        result=browser.find_element_by_css_selector('.news-content>h4').text
        print(result)
    except Exception as err:
        print(err)
    finally:
        browser.close()
        browser.quit()