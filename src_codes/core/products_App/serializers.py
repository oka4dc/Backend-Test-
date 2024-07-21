from rest_framework import serializers
from products_App.models import Products, Cart, Category


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

class CartSerializers(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model =Cart
        fields =[
            "cart_id ",
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




