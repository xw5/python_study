import scrapy
from baidu_img_eye.items import BaiduImgEyeItem

class ImgEyeSpider(scrapy.Spider):
    name = 'img_eye'
    allowed_domains = ['image.baidu.com']
    start_urls = ['https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1630398791088_R&pv=&ic=0&nc=1&z=0&hd=0&latest=0&copyright=0&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E5%A3%81%E7%BA%B8+%E6%8A%A4%E7%9C%BC']

    def parse(self, response):
        img_list = response.xpath('//ul[contains(@class,"imglist")]//a[contains(@class,"imgitem-title")]/@href').extract()
        for item in img_list:
            yield scrapy.Request(response.urljoin(item), callback=self.parse_detail)

    def parse_detail(self, response):
        img_upload = response.xpath('//div[@id="toolbar"]/span[contains(@class, "btn-download")]/@href').extract()
        for item in img_upload:
            item_result = BaiduImgEyeItem()
            item_result['image_urls'] = [response.urljoin(item)]
            yield item_result
