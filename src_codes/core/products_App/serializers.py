from rest_framework import serializers
from products_App.models import Products, Order, Category


class ProductSerializers(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model =Products
        fields =[
            "Product_id"
            "Product_Name",
            "Category",
            "Price",
            "Stock",
            "imageUrl",
            "Created_by",
            "Status",
            "Date_created"
        ]

class OrderSerializers(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model =Order 
        fields =[
            "Order_id",
            "user",
            "created_at",
            "products"
        ]
    
class CartegorySerializers(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model =Category
        fields =[
            "title"
        ] 




