import scrapy
import re
from qfhome.items import QfhomeItem
from scrapy.linkextractors import LinkExtractor

class QfzsSpider(scrapy.Spider):
    name = 'qfzs'
    allowed_domains = ['shenzhen.qfang.com']
    start_urls = ['https://shenzhen.qfang.com/gbasale/b3-b4-k6-pfy10-pty120-f1']

    def parse(self, response):
        for item in response.css('.list-result .items'):
            home_item = QfhomeItem()
            home_item['title'] = item.css('.house-title::attr("title")').extract()[0]
            home_item['link'] = item.css('.house-title::attr("href")').extract()[0]
            house_metas = item.css('.house-metas .meta-items::text').extract()
            home_item['style'] = house_metas[0]
            home_item['area'] = house_metas[1]
            home_item['zx_type'] = house_metas[2]
            home_item['floor'] = re.sub(r'[\s\r\n]+', '', house_metas[3])
            home_item['orientation'] = house_metas[4]
            try:
                home_item['date'] = re.sub(r'[\s\r\n]+', '', house_metas[5])
            except:
                home_item['date'] = ''
            home_item['pos'] = re.sub(r'[\s\r\n]+', '', ''.join(item.css('.house-location .text::text').extract()[0]))
            home_item['total_price'] = item.css('.list-price .amount::text').extract()[0]
            home_item['unit_price'] =item.css('.list-price .smaller::text').extract()[0]
            if len(item.css('.house-tags .school span::text')) > 0:
                home_item['tag'] = item.css('.house-tags .school span::text').extract()[0] + '/' + "/".join(item.css('.house-tags .default::text').extract())
            else:
                home_item['tag'] = "/".join(item.css('.house-tags .default::text').extract())
            yield home_item
            le = LinkExtractor(restrict_css='.page-turning-index')
            links = le.extract_links(response)
            for link in links:
                yield scrapy.Request(link.url)


