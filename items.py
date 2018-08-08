# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OurfirstscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # depends on what info you'd like to store 
    url = scrapy.Field()
    name = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
    contact = scrapy.Field()
