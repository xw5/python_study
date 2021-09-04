# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy


class BaiduImgEyePipeline:
    def process_item(self, item, spider):
        return item


class BaiduImgEyeDownloadPipeline:
    def get_media_requests(self, item, spider):
        for image_url in item.imgurl:
            yield scrapy.Request(image_url, meta={'name': item.name})

    def file_path(self, request, response, spider):
        extstr = request.url.split('.')[-1]
        name = request.meta['name']
        return name + extstr
