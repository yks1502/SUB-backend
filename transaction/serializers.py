from rest_framework import serializers
from user.models import User
from transaction.models import Sale

class SaleSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Sale
    fields = ('id', 'userId', 'created', 'updated', 'title', 'content', 'department', 'bookTitle', 'author', 'publisher', 'price', 'isComplete')
    read_only_fields = ('userId',)