from django.shortcuts import render

from .models import Products, Order

# Create your views here.

def products(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'products/products.html', context)

def product(request, pk):
    product = Products.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'products/product.html', context)

def cart(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        order, created = Order.objects.get_or_create(customer=profile, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
        
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'products/cart.html', context)