# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QfhomeItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    style = scrapy.Field()
    area = scrapy.Field()
    zx_type = scrapy.Field()
    floor = scrapy.Field()
    orientation = scrapy.Field()
    date = scrapy.Field()
    pos = scrapy.Field()
    total_price = scrapy.Field()
    unit_price = scrapy.Field()
    tag = scrapy.Field()