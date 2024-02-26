#from turtle import title
#from unicodedata import name
from .models import OrderItem, User, Cart
from rest_framework import serializers
# from products.models import Products


class UserSerializer(serializers.ModelSerializer):
    orderitem = serializers.StringRelatedField(many=True, read_only=True) 
    class Meta:
        model = User
        fields = ['id','name','email', 'orderitem']



class OrderItemSerializer(serializers.ModelSerializer): 
 
    """Serializer for the OrderItem model."""

    class Meta:
        model = OrderItem
        fields = ['id', 'user','item','quantity']
        # exclude = ['name']

class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields = ['id', 'user', 'products', 'created_at']
        # exclude = ['name']



