from scrapy.selector import Selector

try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle

from houseData.items import HouseDataItem


class AnjukeSpider(CrawlSpider):
    name = "anjuke"
    allowed_domains = ["anjuke.com"]

    start_urls = [
        "http://beijing.anjuke.com/sale"
    ]

    rules = [
        Rule(sle(allow=(r'/sale/p\d+/#filtersort')), follow=True, callback='parse_page')
    ]

    def parse_page(self, response):
        sel = Selector(response)
        for site in sel.css("#houselist-mod > li"):
            item = HouseDataItem()
            item['url'] = site.css("div.house-details > div.house-title > a::attr('href')").extract()
            item['area'] = site.css("div.house-details > div:nth-child(2) > span:nth-child(1)::text").extract()
            item['room_shape'] = site.css("div.house-details > div:nth-child(2) > span:nth-child(3)::text").extract()
            item['average_price'] = site.css("div.house-details > div:nth-child(2) > span:nth-child(5)::text").extract()
            item['floor'] = site.css("div.house-details > div:nth-child(2) > span:nth-child(7)::text").extract()
            item['build_time'] = site.css("div.house-details > div:nth-child(2) > span:nth-child(9)::text").extract()
            item['location'] = site.css("div.house-details > div:nth-child(3) > span::text").extract()
            item['price'] = site.css("div.pro-price > span > strong::text").extract()
            yield item
