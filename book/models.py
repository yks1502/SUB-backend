from django.db import models

class Book(models.Model):
  itemId = models.IntegerField(primary_key=True)
  title = models.CharField(max_length=100)
  publisher = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  priceStandard = models.IntegerField()
  image = models.ImageField()