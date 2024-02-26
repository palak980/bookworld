from django.contrib import admin

# Register your models here.
#from . import models
from .models import Catagory ,Product


#admin.site.register(Catagory)
#admin.site.register(Product)



@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    fields = ('cg','description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name_of_the_product','product_image','price','catagory')
