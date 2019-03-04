# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

from .items import FoodItem


class CrawlFoodPipeline(object):
    def process_item(self, item, spider):
        return item


class FoodItemPipeline:
    collection_name = 'food'

    def __init__(self, mongo_uri=None, mongo_db=None):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.foodset = set()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB', 'items')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, FoodItem):
            self.db[self.collection_name].insert_one(dict(item))
        if item not in self.foodset:
            raise DropItem("Drop duplicated item.")
        return item


class FoodImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        url = item['image_urls'][0]
        path = '{}/{}.jpg'.format(item['category'],
                                  item['name'])
        return [Request(url, meta={'path': path})]

    def file_path(self, request, response=None, info=None):
        return request.meta.get('path')

    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no files")
        item['food_image_path'] = file_paths[0]
        return item

