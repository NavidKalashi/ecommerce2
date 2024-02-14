from django.shortcuts import render
from django.http import HttpResponse

from .models import Products

# Create your views here.

def products(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'products/products.html', context)

def product(request, pk):
    product = Products.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'products/product.html', context)