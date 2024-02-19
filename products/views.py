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
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items': items}
    return render(request, 'products/cart.html', context)