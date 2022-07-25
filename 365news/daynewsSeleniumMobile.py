# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

mobile_emulation = {"deviceName": "iPhone XR"}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)  # 这里看清楚了，不是add_argument

browser = webdriver.Chrome(executable_path=r'E:\study\python\python_reptile\selenium_pro\chromedriver_win32\chromedriver.exe',
                          options=chrome_options)

browser.get("https://www.163.com/dy/media/T1603594732083.html")

element = browser.find_element(By.XPATH, "//div[contains(@class,'m-viewpoint')][1]")
newUrl = element.get_attribute('data-href')
browser.get('https://'+newUrl)

# all_windows = browser.window_handles
# browser.switch_to.window(all_windows[-1])
element_news = browser.find_element(By.XPATH, "//div[@class='m-viewpoint']")
element_news.screenshot('news.png')

browser.get("https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner")

element_xg = browser.find_element(By.XPATH, "//div[@id='ptab-0']/div[1]")
element_xg.screenshot('xg.png')
