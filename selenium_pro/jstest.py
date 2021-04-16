# coding=utf-8
from selenium import webdriver
import time,os

driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
file_path = 'file:///' + os.path.abspath('jstest.html')
driver.get(file_path)
# 通过JS 隐藏选中的元素
# 第一种方法：
time.sleep(3)
driver.execute_script('$("#tooltip").fadeOut();')
time.sleep(3)
# 第二种方法：
button = driver.find_element_by_class_name('btn')
driver.execute_script('$(arguments[0]).fadeOut()', button)
time.sleep(3)
driver.execute_script('document.write("selenium自动化NB")')
time.sleep(3)

driver.quit()
