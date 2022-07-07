# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome(executable_path=r'E:\study\python\python_reptile\selenium_pro\chromedriver_win32\chromedriver.exe')

browser.get("https://www.163.com/dy/media/T1603594732083.html")

element = browser.find_element(By.XPATH, "//div[@class='tab_content']/ul[@class='list_box cur']/li/a")

element.click()
time.sleep(5)
all_windows = browser.window_handles
browser.switch_to.window(all_windows[-1])
element_news = browser.find_element(By.XPATH, "//div[@class='post_body']/p[2]")
element_news.screenshot('news.png')

browser.get("https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner")

element_xg = browser.find_element(By.CLASS_NAME, 'VirusSummarySix_1-54-1_ZRHUKw')
element_xg.screenshot('xg.png')

