from django.urls import path
from products_App.views import productCreateRetreiveAll, ProductDetail, OrderViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products_App.views import OrderViewSet



router = DefaultRouter()
#router.register(r'categories', CategoryViewSet)
#router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orders/place_order/', OrderViewSet.as_view({'post': 'place_order'}), name='place_order'),
    path('orders/order_history/', OrderViewSet.as_view({'get': 'order_history'}), name='order_history'),
    path('CreateProduct/', productCreateRetreiveAll.as_view(), name='CreateProduct'),
    path('products/', productCreateRetreiveAll.as_view(), name='products'),
    path('DeleteProduct/', ProductDetail.as_view(), name='DeleteProduct'),
    path('UpdateProduct/', ProductDetail.as_view(), name='UpdateProduct'),
]