from rest_framework import serializers

from user.models import User
from transaction.models import Sale, Purchase

class UserSerializer(serializers.ModelSerializer):
  sale_owner = serializers.PrimaryKeyRelatedField(many=True, queryset=Sale.objects.all())
  purchase_owner = serializers.PrimaryKeyRelatedField(many=True, queryset=Purchase.objects.all())
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'nickname', 'isConfirmed', 'created', 'updated', 'confirmationToken',
    'sale_owner', 'purchase_owner')

class NicknameSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'nickname')