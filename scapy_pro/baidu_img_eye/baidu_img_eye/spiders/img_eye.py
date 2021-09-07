import scrapy
from baidu_img_eye.items import BaiduImgEyeItem

class ImgEyeSpider(scrapy.Spider):
    name = 'img_eye'
    allowed_domains = ['image.baidu.com']
    start_urls = ['https://image.baidu.com/search/index?ct=&z=0&tn=baiduimage&ipn=r&word=%E5%A3%81%E7%BA%B8%20%E6%8A%A4%E7%9C%BC&pn=0&istype=2&ie=utf-8&oe=utf-8&cl=&lm=-1&st=-1&fr=&fmq=1630398791088_R&ic=4&se=&sme=&width=1920&height=1080&face=0&hd=0&latest=0&copyright=0']

    def parse(self, response):
        img_list = response.xpath('//ul[contains(@class,"imglist")]//a[contains(@class,"imgitem-title")]/@href').extract()
        for item in img_list[0:5]:
            yield scrapy.Request(response.urljoin(item), callback=self.parse_detail)

    def parse_detail(self, response):
        img_upload = response.xpath('//div[@id="toolbar"]/span[contains(@class, "btn-download")]/@href').extract()
        img_name = response.xpath('//div[@id="picInfoPnl"]//div[@class="pic-title"]/span/text()').extract()
        item_result = BaiduImgEyeItem()
        item_result['imgurl'] = response.urljoin(img_upload[0])
        item_result['name'] = img_name[0]
        yield item_result
