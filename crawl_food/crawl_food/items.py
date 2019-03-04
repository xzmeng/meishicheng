# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlFoodItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FoodItem(scrapy.Item):
    category = scrapy.Field()
    name = scrapy.Field()
    intro = scrapy.Field()
    gongyi = scrapy.Field()  # 美食工艺
    kouwei = scrapy.Field()  # 美食口味
    ingredients = scrapy.Field()  # 用料

    images = scrapy.Field()
    image_urls = scrapy.Field()
    food_image_path = scrapy.Field()

