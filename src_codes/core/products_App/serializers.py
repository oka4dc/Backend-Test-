from rest_framework import serializers
from products_App.models import Products, Category


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




