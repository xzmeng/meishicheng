from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # 创建新的订单
    path('create/', views.order_create, name='order_create'),
    # 管理员可以执行，查看订单列表和导出到pdf
    path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
    path('admin/order/<int:order_id>/pdf/', views.admin_order_pdf, name='admin_order_pdf'),
]
