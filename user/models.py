from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  nickname = models.CharField(
    max_length=12,
    unique=True,
    blank=True,
  )
  isConfirmed = models.BooleanField(
    default=False,
  )
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('id',)