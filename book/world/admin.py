from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(booksmodel)
class booksadmin(admin.ModelAdmin):
    
    fields = ['__all__']
