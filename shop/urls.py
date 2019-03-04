from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('order_list/', views.order_list, name='order_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('rest/<str:restaurant_name>/', views.product_list,
         name='product_list_by_restaurant'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('other/search', views.search_food, name='search'),
]