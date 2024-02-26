from django.db import models
from django.conf import settings
from sem_course.models import Product
# Create your models here.



class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    #created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return "{}".format(self.name)

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name= 'orderitem')
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0)
    
    #created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        #return "{}".format(self.item)
        # return "{} - {}".format(self.item, self.user)
        return "{} -  {}".format(self.item, self.quantity)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ManyToManyField(OrderItem, max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return "{}".format(self.user)


