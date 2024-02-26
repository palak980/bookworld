from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.
CATAGORY_CHOICE = ((
    ('Surprise Meal','Surprise Meal'),
    ('Bowls','Bowls'),
    ('Superbowls','Superbowls'),
    ('Pastas & Steaks','Pastas & Steaks'),
    ('Fit N Fab','Fit N Fab'),
    ('Thalis','Thalis'),
    ('Sandwiches','Sandwiches'),
    ('Wrapes','Wrapes'),
    ('Burgers','Burgers'),
    ('Appetizer','Appetizer'),
    ('Desserts','Desserts'),
    ('All Day Breakfast','All Day Breakfast'),
    ('Beverages','Beverages'),# first value is for storing and 2nd value for showing

))



class Catagory(models.Model):
    cg = models.CharField(choices=CATAGORY_CHOICE,max_length=50,unique=True)
    description = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.cg


class Product(models.Model):
    name_of_the_product = models.CharField(max_length=20,unique=True,null=True,blank=True)
    product_image = models.ImageField(upload_to='images/' ,default=None,null=True)
    price = models.CharField(max_length=20,unique=True,null=True,blank=True)
    
    catagory = models.ForeignKey(Catagory,on_delete=models.PROTECT,related_name="product")

    def __str__(self) -> str:
        return self.name_of_the_product

    
    
    