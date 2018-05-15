from django.db import models
from user.models import User

class Sale(models.Model):
  userId = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=100, default='')
  content = models.CharField(max_length=2000, default='')
  department = models.CharField(max_length=20, default='')
  bookTitle = models.CharField(max_length=50, default='')
  author = models.CharField(max_length=50, default='')
  publisher = models.CharField(max_length=50, default='')
  price = models.IntegerField()
  isComplete = models.BooleanField(default=False)

  class Meta:
    ordering = ('id',)

  def save(self, *args, **kwargs):
    super(Sale, self).save(*args, **kwargs)