from .cart import Cart


# 在模板引擎中使用cart 时会调用该函数, 取出我们在session保存的Cart实例
def cart(request):
    return {'cart': Cart(request)}
