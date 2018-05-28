from django.db import models

from user.models import User

class Sale(models.Model):
  user = models.ForeignKey(User, related_name='sale_owner', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=100, default='')
  content = models.CharField(max_length=2000, default='')
  department = models.CharField(max_length=20, default='')
  bookTitle = models.CharField(max_length=50, default='')
  author = models.CharField(max_length=50, default='')
  publisher = models.CharField(max_length=50, default='')
  price = models.IntegerField()
  isComplete = models.BooleanField(default=False)
  
  class Meta:
    ordering = ('-created',)

class Purchase(models.Model):
  user = models.ForeignKey(User, related_name='purchase_owner', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=100, default='')
  content = models.CharField(max_length=2000, default='')
  department = models.CharField(max_length=20, default='')
  bookTitle = models.CharField(max_length=50, default='')
  author = models.CharField(max_length=50, default='')
  publisher = models.CharField(max_length=50, default='')
  price = models.IntegerField()
  isComplete = models.BooleanField(default=False)

  class Meta:
    ordering = ('-created',)

class SaleComment(models.Model):
  user = models.ForeignKey(User, related_name='sale_comment_owner', on_delete=models.CASCADE)
  postId = models.ForeignKey(Sale, related_name='sale_of_comment', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  content = models.CharField(max_length=2000)

  class Meta:
    ordering = ('created',)

class PurchaseComment(models.Model):
  user = models.ForeignKey(User, related_name='purchase_comment_owner', on_delete=models.CASCADE)
  postId = models.ForeignKey(Purchase, related_name='purchase_of_comment', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  content = models.CharField(max_length=2000)

  class Meta:
    ordering = ('created',)
    