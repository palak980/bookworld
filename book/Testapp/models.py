from django.db import models

# Create your models here.
class Search(models.Model):
    location = models.CharField(max_length=50) 
    services = models.CharField(max_length=50)

