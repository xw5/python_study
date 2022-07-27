# coding = utf-8
from selenium import webdriver

import time
browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.maximize_window()
browser.get("http://10.51.104.185:8080/login")

browser.implicitly_wait(5)

browser.find_element_by_name('j_username').send_keys("admin")
time.sleep(0.3)
browser.find_element_by_name("j_password").send_keys("1234.abcd")
time.sleep(0.3)
browser.find_elements_by_class_name('submit-button')[0].click()