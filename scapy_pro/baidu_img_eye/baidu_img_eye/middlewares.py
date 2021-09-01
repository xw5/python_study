# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from scrapy.http import HtmlResponse

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

class SeleniumDownloadMiddleware(object):
    def __init__(self):
        chrome_options = Options() # 模拟器设置
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe', options=chrome_options)

    def process_request(self, request, spider):
        self.driver.get(request.url)
        time.sleep(5)
        source = self.driver.page_source
        print(source)
        response = HtmlResponse(url=self.driver.current_url, body=source, request=request, encoding='utf-8')
        return response
