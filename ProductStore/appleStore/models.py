from django.db import models


class Product(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='product_img/')
