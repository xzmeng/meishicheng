import redis
from django.conf import settings
from .models import Product

r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db=settings.REDIS_DB)


# Recommender实现了食物推荐
# 用到了redis中的有序集合zset, 该集合中的元素为字符串, 每个字符串都可以关联一个double类型的数字,
# 集合中元素根据数字大小进行排序
# 根据这个特性可以对每个食物创建一个集合, 该集合中的元素为跟这个食物产生过一起购买行为的食物,
# 元素的关联数字为该元素与该食物(集合名)产生一同购买行为的次数，从而可以描述两者的关联性

# 进行推荐时的方法为:
# 当进入一个食物详情页面时, 推荐该食物对应zset中一同购买次数最多的食物中的前四个
# 当进入购物车中, 对购物车中的所有食物的集合进行一个zunionstore操作, 选取新集合中前四个
# 对多个集合进行zunionstore会把相同的元素名相加.

class Recommender(object):
    # connect to redis

    def get_product_key(self, id):
        return 'product:{}:purchased_with'.format(id)

    def products_bought(self, product_ids):
        # product_ids = [p.id for p in products]
        for product_id in product_ids:
            for with_id in product_ids:
                # 获取与每一个食物一同购买的其他食物的id
                if product_id != with_id:
                    # 增加一同购买的计数
                    r.zincrby(self.get_product_key(product_id),
                              1,
                              with_id,
                              )

    def suggest_products_for(self, products, max_results=6):
        product_ids = [p.id for p in products]
        if len(products) == 1:
            # 只有一个食物(食物详情页面)
            suggestions = r.zrange(
                             self.get_product_key(product_ids[0]),
                             0, -1, desc=True)[:max_results]
        else:
            # 产生一个临时的key
            flat_ids = ''.join([str(id) for id in product_ids])
            tmp_key = 'tmp_{}'.format(flat_ids)
            # 对多个食物的计数进行union, 把结果存储在临时的集合tmp_key中
            keys = [self.get_product_key(id) for id in product_ids]
            r.zunionstore(tmp_key, keys)
            # 删除购买的食物本身
            r.zrem(tmp_key, *product_ids)
            # 获取最大的tmp_key中最大的四个
            suggestions = r.zrange(tmp_key, 0, -1, 
                                   desc=True)[:max_results]
            # 删除刚才生成的临时集合
            r.delete(tmp_key)
        suggested_products_ids = [int(id) for id in suggestions]

        # 获取推荐食物列表
        suggested_products = list(Product.objects.filter(id__in=suggested_products_ids))
        suggested_products.sort(key=lambda x: suggested_products_ids.index(x.id))
        return suggested_products

    def clear_purchases(self):
            for id in Product.objects.values_list('id', flat=True):
                r.delete(self.get_product_key(id))

