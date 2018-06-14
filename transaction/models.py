from django.db import models

from user.models import User
from book.models import Book

class Sale(models.Model):
  user = models.ForeignKey(User, related_name='my_sale', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=100)
  content = models.CharField(max_length=10000)
  department = models.CharField(max_length=20)
  bookTitle = models.CharField(max_length=200)
  author = models.CharField(max_length=1000)
  publisher = models.CharField(max_length=100)
  price = models.IntegerField()
  isComplete = models.BooleanField(default=False)
  contact = models.CharField(max_length=50)
  image = models.ImageField()
  book = models.ForeignKey(Book, related_name='sale', on_delete=models.CASCADE, null=True, blank=True)

  class Meta:
    ordering = ('-created',)

class Purchase(models.Model):
  user = models.ForeignKey(User, related_name='my_purchase', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=100)
  content = models.CharField(max_length=10000)
  department = models.CharField(max_length=20)
  bookTitle = models.CharField(max_length=200)
  author = models.CharField(max_length=1000)
  publisher = models.CharField(max_length=100)
  price = models.IntegerField()
  isComplete = models.BooleanField(default=False)
  contact = models.CharField(max_length=50)
  book = models.ForeignKey(Book, related_name='purchase', on_delete=models.CASCADE, null=True, blank=True)

  class Meta:
    ordering = ('-created',)

class SaleComment(models.Model):
  user = models.ForeignKey(User, related_name='sale_comment_owner', on_delete=models.CASCADE)
  postId = models.ForeignKey(Sale, related_name='sale_comments', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  content = models.CharField(max_length=2000)

  class Meta:
    ordering = ('created',)

class PurchaseComment(models.Model):
  user = models.ForeignKey(User, related_name='purchase_comment_owner', on_delete=models.CASCADE)
  postId = models.ForeignKey(Purchase, related_name='purchase_comments', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  content = models.CharField(max_length=2000)

  class Meta:
    ordering = ('created',)

class SaleInterest(models.Model):
  user = models.ForeignKey(User, related_name='my_interest_sale', on_delete=models.CASCADE)
  sale = models.ForeignKey(Sale, related_name='sale_interest', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    unique_together = (('user', 'sale'),)
    ordering = ('created',)

class PurchaseInterest(models.Model):
  user = models.ForeignKey(User, related_name='my_interest_purchase', on_delete=models.CASCADE)
  purchase = models.ForeignKey(Purchase, related_name='purchase_interest', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    unique_together = (('user', 'purchase'),)
    ordering = ('created',)

class SaleAlarm(models.Model):
  user = models.ForeignKey(User, related_name='sale_alarm', on_delete=models.CASCADE)
  sale = models.ForeignKey(Sale, related_name='sale_alarm_owner', on_delete=models.CASCADE)

  class Meta:
    ordering = ('id',)

class PurchaseAlarm(models.Model):
  user = models.ForeignKey(User, related_name='purchase_alarm', on_delete=models.CASCADE)
  purchase = models.ForeignKey(Purchase, related_name='purchase_alarm_owner', on_delete=models.CASCADE)

  class Meta:
    ordering = ('id',)