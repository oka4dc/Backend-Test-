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
    Name = models.CharField(max_length=100)
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


