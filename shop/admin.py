from django.contrib import admin
from .models import Category, Product, Restaurant

# 使用django自带的后台管理系统
# djangok可以对已有的Model自动生成管理界面
# 直接 admin.site.register(<model name>) 添加到admin.py中就行了
# 如果要对管理页面进行定制, 则需要创建admin.ModelAdmin的子类
# 并且添加 admin.register(<model name>) 装饰器, 就像下面这样
# 具体的定制行为文档上很详细


# 将Category添加到管理页面
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']    # 显示的字段,只有这些会显示在管理界面上
    prepopulated_fields = {'slug': ('name',)}
    # 自动填充, 在页面上手动添加内容时, slug字段会根据name自动进行填充


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    name = '菜名'
    list_display = ['name', 'slug', 'restaurant', 'price',
                    'available', 'created', 'updated']
    list_filter = ['restaurant', 'category']  # 过滤器, 可以根据店铺和食物种类来进行筛选
    list_editable = ['price', 'available']  # 可以在管理页面修改的字段
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass


admin.site.site_header = '中华美食城管理系统'