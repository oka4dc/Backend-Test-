from django.urls import path
from products_App.views import productCreateRetreiveAll, ProductDetail
from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('CreateProduct/', productCreateRetreiveAll.as_view(), name='CreateProduct'),
    path('products/', productCreateRetreiveAll.as_view(), name='products'),
    path('DeleteProduct/', ProductDetail.as_view(), name='DeleteProduct'),
    path('UpdateProduct/', ProductDetail.as_view(), name='UpdateProduct'),
]