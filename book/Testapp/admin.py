from django.contrib import admin
from .models import Search

# Register your models here.
@admin.register(Search)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['location','services']
