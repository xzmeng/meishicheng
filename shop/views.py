from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from orders.models import Order
from .models import Category, Product, Restaurant
from cart.forms import CartAddProductForm
from .recommender import Recommender
from django.core.paginator import Paginator
from .forms import SearchForm


def product_list(request, category_slug=None,
                 restaurant_name=None):
    category = None
    restaurant = None
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    if restaurant_name:
        restaurant = get_object_or_404(Restaurant, name=restaurant_name)
        products = products.filter(restaurant=restaurant)

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
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'recommended_products': recommended_products})


@login_required
def order_list(request):
    order_list = Order.objects.filter(user=request.user)

    return render(request,
                  'shop/info/order_list.html',
                  {'order_list': order_list})


def search_food(request):
    search_name = request.GET.get('search_name')
    food_list = Product.objects.filter(name__contains=search_name)
    paginator = Paginator(food_list, 20)
    page = request.GET.get('page', 1)
    products = paginator.get_page(page)
    return render(request,
                  'shop/product/search.html',
                  {'products': products,
                   'search_name': search_name,
                   'page': page})
