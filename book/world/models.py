from django.db import models

# Create your models here.
class booksmodel(models.Model):
    name=models.CharField(max_length=250)
    author=models.CharField(max_length=500)
    date=models.DateTimeField()
    photo=models.ImageField(upload_to=None,null=True)
    price=models.IntegerField()
    quantity=models.IntegerField()
    des=models.CharField(max_length=500)
    def __str__(self):
        return self.name