from django.db import models
from django.urls import reverse

# class Category(models.Model):
#     name = models.CharField(max_length=200,
#                             db_index=True)
#     slug = models.SlugField(max_length=200,
#                             unique=True)
#
#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#             return reverse('shop:product_list_by_category',
#                            args=[self.slug])


# class Product(models.Model):
#     category = models.ForeignKey(Category,
#                                  related_name='products',
#                                  on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True)
#     image = models.ImageField(upload_to='products/%Y/%m/%d',
#                               blank=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ('name',)
#         index_together = (('id', 'slug'),)
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#             return reverse('shop:product_detail',
#                            args=[self.id, self.slug])


class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = '菜系'
        verbose_name_plural = '菜系'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shop:product_list_by_category',
                           args=[self.slug])


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
    name = models.CharField(max_length=200, db_index=True)
    kouwei = models.CharField(max_length=50)
    gongyi = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=35.00)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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
