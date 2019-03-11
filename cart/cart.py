from decimal import Decimal
from django.conf import settings
from shop.models import Product


# 购物车
class Cart(object):

    def __init__(self, request):
        """
        初始化购物车
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # 将空的购物车保存到session中
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        遍历购物车中的所有商品并且将他们的信息从数据库中取出来
        """
        product_ids = self.cart.keys()
        # 在数据库中将商品拿出来并且添加到购物车中
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    
    def __len__(self):
        """
        计数
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        """
        将商品添加到购物车或者更新商品数量
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                      'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # 将session标记为modified来保证更新可以得到保存
        self.session.modified = True

    def remove(self, product):
        """
        将商品从购物车中删除
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # 从session中删除购物车
        del self.session[settings.CART_SESSION_ID]
        self.save()
