from django.db.models import fields
from rest_framework import serializers
from .models import *
  
class booksSerializer(serializers.ModelSerializer):
    class Meta:
        model = booksmodel
        fields = ('__all__')