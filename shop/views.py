from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from orders.models import Order
from .models import Category, Product, Restaurant
from cart.forms import CartAddProductForm
from .recommender import Recommender
from django.core.paginator import Paginator
from .forms import SearchForm


# views.py中的每一个函数都对应一个页面请求
# 每个视图函数接受一个 request 参数, 代表http_request
# 一般会返回 render(<template name>, 参数字典)
def product_list(request, category_slug=None,
                 restaurant_name=None):
    category = None
    restaurant = None
    # 获取所有种类， 餐厅， 食物
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    products = Product.objects.filter(available=True)
    # 如果指定了类别，则只选择该类别的书屋
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    # 如果指定了餐厅，只选择该餐厅的食物
    if restaurant_name:
        restaurant = get_object_or_404(Restaurant, name=restaurant_name)
        products = products.filter(restaurant=restaurant)

    # django内置的分页器
    paginator = Paginator(products, 20)
    page = request.GET.get('page', 1)
    products = paginator.get_page(page)
    search_form = SearchForm()
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'restaurant': restaurant,
                   'restaurants': restaurants,
                   'products': products,
                   'form': search_form})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    # 创建一个购物车添加表单
    cart_product_form = CartAddProductForm()
    # 添加推荐器并且根据该食物进行推荐
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'recommended_products': recommended_products})


# 必须登陆才能访问，用到了内置的用户系统
@login_required
def order_list(request):
    # 显示订单列表
    order_list = Order.objects.filter(user=request.user)

    return render(request,
                  'shop/info/order_list.html',
                  {'order_list': order_list})


# 搜索食物
def search_food(request):
    search_name = request.GET.get('search_name')
    food_list = Product.objects.filter(name__contains=search_name)
    # name__contains 表示name字段包含
    paginator = Paginator(food_list, 20)
    page = request.GET.get('page', 1)
    products = paginator.get_page(page)
    return render(request,
                  'shop/product/search.html',
                  {'products': products,
                   'search_name': search_name,
                   'page': page})
