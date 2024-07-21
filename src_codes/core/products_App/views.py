from django.shortcuts import render
from products_App.models import Order, Category, Products
from rest_framework import status
from rest_framework.views import APIView
from products_App.serializers import CartegorySerializers, ProductSerializers, OrderSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
# Create your views here.
from rest_framework.response import Response


class productCreateRetreiveAll(APIView):
    """Create and get all products

    Args:
        APIView (_type_): _description_
    """
    def post (self, request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        user = Products.objects.all()
        serializer = ProductSerializers(user, many = True)
        return Response(data=serializer.data, status= status.HTTP_200_OK)
    
class ProductDetail(APIView):
    """Retrieve, update or delete a product from the database

    Args:
        APIView (_type_): _description_
    """
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except:
            raise Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk, format = None):
        product = self.get_object(pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        products = self.get_object(pk)
        serializer = ProductSerializers(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        

class CatergoryCreateRetreiveAll(APIView):
    """Create and get all products

    Args:
        APIView (_type_): _description_
    """
    def post (self, request):
        serializer = CartegorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        categories = Category.objects.all()
        serializer = CartegorySerializers(categories, many = True)
        return Response(data=serializer.data, status= status.HTTP_200_OK)
    
class CatergoryDetail(APIView):
    """Retrieve, update or delete a Catergory from the database

    Args:
        APIView (_type_): _description_
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except:
            raise Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk, format = None):
        product_cart = self.get_object(pk)
        serializer = ProductSerializers(product_cart)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        product_cart = self.get_object(pk)
        serializer = CartegorySerializers(product_cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product_cart = self.get_object(pk)
        product_cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        

class Order(APIView):
    """_summary_

    Args:
        APIView (_type_): _description_
    """
    def place_order(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def order_history(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)



