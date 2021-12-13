# coding = utf-8
from selenium import webdriver

import time
browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.maximize_window()
browser.get("https://im.ygsoft.com/works/#/login")

browser.implicitly_wait(5)

browser.find_element_by_css_selector('.user-info input[type="text"]').send_keys("xiewu@ygsoft.com")
time.sleep(0.3)
browser.find_element_by_css_selector('.user-info input[type="password"]').send_keys("YG19870120xw4")
time.sleep(0.3)
browser.find_element_by_css_selector('.login-btn-box button').click()