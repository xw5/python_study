import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        filename = "teacher.html"
        print('-'*50)
        print(response)
        open(filename, 'w', encoding='utf-8').write(response.text)
