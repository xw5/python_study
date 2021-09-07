# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
# from scrapy.exceptions import DropItem

class BaiduImgEyePipeline:
    def process_item(self, item, spider):
        return item


class BaiduImgEyeDownloadPipeline:
    def get_media_requests(self, item, spider):
        print('-----', item)
        yield scrapy.Request(item.imgurl, meta={'name': item.name})

    def file_path(self, request, response, spider):
        extstr = request.url.split('.')[-1]
        name = request.meta['name']
        return name + extstr
