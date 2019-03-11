import random
from xpinyin import Pinyin
from django.utils.text import slugify

import pymongo
from django.core.management.base import BaseCommand, CommandError
from shop.models import Category, Product, Restaurant
from xpinyin import Pinyin


# 这个类创建了 python manage.py convert 命令
# 该命令将mongodb中的食物数据倒入到关系数据库中
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
        # 虚构了几个餐厅
        restaurants = ['阿坤私房菜', '橘子餐厅', '北欧时光·清真',
                       '辣一天川小館', '川人百味']
        categories = [Category(name=cat, slug=pin.get_pinyin(cat)) for cat in categories]
        restaurants = [Restaurant(name=res) for res in restaurants]
        for category in categories:
            category.save()
        for res in restaurants:
            res.save()
        for category in categories:
            for food in db.food.find({'category': category.name}):
                product = Product.objects.create(
                    category=category,
                    name=food['name'],
                    slug=slugify(pin.get_pinyin(food['name'])),
                    image='/static/food_images/{}/{}.jpg'.format(
                        category.name, food['name']
                    ),
                    kouwei=food['kouwei'],
                    gongyi=food['gongyi'],
                    restaurant=random.choice(restaurants),
                    description=food['intro'] or 'no description.',
                    price=random.randint(10, 100))
                product.save()
