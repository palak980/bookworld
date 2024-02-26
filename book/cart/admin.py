from django.contrib import admin

# Register your models here.
from .models import OrderItem, User, Cart

# admin.site.register(User)
# admin.site.register(Cart)
# admin.site.register(OrderItem)
# admin.site.register(DeliveryCost)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    fields = ['user','item','quantity']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['name','email']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    fields = ['user','products']