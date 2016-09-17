# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseDataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    community = scrapy.Field()
    location = scrapy.Field()
    build_time = scrapy.Field()
    type = scrapy.Field()
    room_shape = scrapy.Field()
    area = scrapy.Field()
    floor = scrapy.Field()
    decorate = scrapy.Field()
    average_price = scrapy.Field()
    price = scrapy.Field()


