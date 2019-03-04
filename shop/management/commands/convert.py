import random
from xpinyin import Pinyin
from django.utils.text import slugify

import pymongo
from django.core.management.base import BaseCommand, CommandError
from shop.models import Category, Product
from xpinyin import Pinyin


class Command(BaseCommand):
    def handle(self, *args, **options):
        pin = Pinyin()
        MONGO_URI = 'mongodb://localhost:27017'
        MONGO_DB = 'chinese_food'
        mongo_client = pymongo.MongoClient(MONGO_URI)
        db = mongo_client[MONGO_DB]
        categories = set()
        for food in db.food.find({}):
            categories.add(food['category'])
        categories = list(categories)
        categories = [Category(name=cat, slug=pin.get_pinyin(cat)) for cat in categories]
        for category in categories:
            category.save()
        for category in categories:
            for food in db.food.find({'category': category.name}):
                product = Product.objects.create(
                    category=category,
                    name=food['name'],
                    slug=slugify(pin.get_pinyin(food['name'])),
                    image='/static/food_images/{}/{}.jpg'.format(
                        category.name, food['name']
                    ),
                    description=food['intro'] or 'no description.',
                    price=random.randint(10, 100))
                product.save()
