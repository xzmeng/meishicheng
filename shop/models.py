from django.db import models
from django.urls import reverse


# orm映射, django的migrate功能会自动根据每个app中models.py的内容
# 在相应后端如mysql中创建对应的表


class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)

    # SlugField可以优雅地表示url中,只允许字母数字横线(-),比如鱼香肉丝的slug为
    # yu-xiang-rou-si
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)  # 查询结果默认根据name排序
        verbose_name = '菜系'  # 显示在后台界面时label的名字
        verbose_name_plural = '菜系'  # 复数形式

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shop:product_list_by_category',
                           args=[self.slug])
            # 获取该对象的url, 具体可见 views.product_list_by_category()


class Restaurant(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shop:product_list_by_restaurant',
                           args=[self.name])

    class Meta:
        verbose_name = '餐厅'
        verbose_name_plural = '餐厅列表'


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,
                                   related_name='products',
                                   on_delete=models.CASCADE)
    # 定义一个外键盘, related_name只会在django中起作用，可以方便地通过
    # Restaurant的实例查询其所拥有的菜, 但是不会在数据库中增加任何额外信息

    # on_delete 定义了如果这个外键对应的对象(数据行)删除后会发生的结果
    # CASCADE表示所有关联的食物都会被一起删除, 其他的如SET_NULL可以将该键置空而不是删除对象

    name = models.CharField(max_length=200, db_index=True)
    kouwei = models.CharField(max_length=50)
    gongyi = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=35.00)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)  # auto_now_add创建新的行时该字段自动设置为当前时间
    updated = models.DateTimeField(auto_now=True)  # 创建或者修改时自动设置为当前时间

    class Meta:
        verbose_name = '菜品'
        verbose_name_plural = '菜品列表'
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shop:product_detail',
                           args=[self.id, self.slug])
