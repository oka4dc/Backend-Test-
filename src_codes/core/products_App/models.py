from django.db import models
from django.contrib.auth.models import User
from User_App.models import CustomUser
# Create your models here.

class Category(models.Model):
    """Define parameters for creating product catergory

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title


class Products(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    Product_id = models.CharField(max_length=10)
    Product_Name = models.CharField(max_length=100)
    Category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    Price = models.IntegerField()
    Stock = models.IntegerField()
    imageUrl = models.URLField()
    Created_by = models.ForeignKey(CustomUser, related_name='products', on_delete=models.CASCADE)
    Status = models.BooleanField(default=True)
    Date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['Date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)


class Cart(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    cart_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Products)

    class Meta:
        ordering = ['cart_id', '-created_at']
        

    def __str__(self):
        return f'{self.cart_id}'