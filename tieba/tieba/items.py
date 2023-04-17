# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebaItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    author_level = scrapy.Field()
    reply = scrapy.Field()
    link = scrapy.Field()
    ip = scrapy.Field()
    os = scrapy.Field()
    # timestamp = scrapy.Field()
    pass
