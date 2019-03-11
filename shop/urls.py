from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # 食物列表
    path('', views.product_list, name='product_list'),
    # 订单列表
    path('order_list/', views.order_list, name='order_list'),
    # 按照分类显示
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    # 按照餐厅显示
    path('rest/<str:restaurant_name>/', views.product_list,
         name='product_list_by_restaurant'),
    # 食物详情
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    # 搜索
    path('other/search', views.search_food, name='search'),
]