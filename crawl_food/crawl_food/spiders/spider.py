# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from ..items import FoodItem


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['meishij.net']
    start_urls = [
        'https://www.meishij.net/china-food/caixi/']

    def parse(self, response):
        links = response.css("#listnav > div > dl dd a::attr(href)").getall()
        for link in links:
            yield response.follow(link, callback=self.parse_one_page)

    def parse_one_page(self, response):
        category = response.css("#listnav > div > dl > dd.current > h1 > a::text").get()
        links = response.css("#listtyle1_list a::attr(href)").getall()
        for link in links:
            yield response.follow(link, callback=self.parse_food, meta={'category': category})
        next_page = response.css('.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse_one_page)

    def parse_food(self, response):
        item = FoodItem()
        item['category'] = response.meta['category']
        item['name'] = response.css('h1 a::text').get()
        item['intro'] = response.css('.materials p::text').get()
        item['gongyi'] = response.css('#tongji_gy::text').get()
        item['kouwei'] = response.css('#tongji_kw::text').get()
        item['ingredients'] = response.css('.materials_box .zl h4 a::text').getall()
        item['image_urls'] = [response.css('.cp_headerimg_w img::attr(src)').get()]
        yield item
