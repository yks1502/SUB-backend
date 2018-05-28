from rest_framework import serializers

from user.models import User
from transaction.models import Sale, Purchase

class UserSerializer(serializers.ModelSerializer):
  my_sale = serializers.PrimaryKeyRelatedField(many=True, queryset=Sale.objects.all())
  my_purchase = serializers.PrimaryKeyRelatedField(many=True, queryset=Purchase.objects.all())
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'nickname', 'isConfirmed', 'created', 'updated', 'confirmationToken',
    'my_sale', 'my_purchase')

class NicknameSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'nickname')