from rest_framework import serializers
from .models import *


# class CatagorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Catagory
#         fields =  "__all__"


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields =["name_of_the_product","product_image","price","catagory"]

        
# class SemProductSerializer(serializers.ModelSerializer):
#     product = ProductSerializer(many = True,read_only = True)
#     class Meta:
#         model = Catagory
#         fields = ["cg"]
class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = ['id','cg','description']
         

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name_of_the_product','product_image','price','catagory']
         