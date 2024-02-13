from django.urls import path

from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('product/<int:pk>/', views.product, name='product'),
]
