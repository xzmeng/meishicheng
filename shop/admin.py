from django.contrib import admin
from .models import Category, Product, Restaurant


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    name = '菜名'
    list_display = ['name', 'slug', 'restaurant', 'price',
                    'available', 'created', 'updated']
    list_filter = ['restaurant', 'category']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


# class ProductInline(admin.TabularInline):
#     model = Product
#     raw_id_fields = ['restaurant']


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    # inlines = [ProductInline]
    pass

admin.site.site_header = '中华美食城管理系统'