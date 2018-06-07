from rest_framework import serializers

from user.models import User
from transaction.models import Sale, Purchase, SaleInterest, PurchaseInterest

class UserSerializer(serializers.ModelSerializer):
  my_sale = serializers.PrimaryKeyRelatedField(many=True, queryset=Sale.objects.all())
  my_purchase = serializers.PrimaryKeyRelatedField(many=True, queryset=Purchase.objects.all())
  my_interest_sale = serializers.PrimaryKeyRelatedField(many=True, queryset=Sale.objects.all())
  my_interest_purchase = serializers.PrimaryKeyRelatedField(many=True, queryset=Purchase.objects.all())
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'nickname', 'isConfirmed', 'created', 'updated', 'confirmationToken',
    'my_sale', 'my_purchase', 'my_interest_sale', 'my_interest_purchase')

class NicknameSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'nickname')

class UserSaleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sale
    fields = ('id', 'created', 'updated',
    'title', 'content', 'department', 'bookTitle', 'author', 'publisher', 'price', 'isComplete',
    'sale_comments')

class UserPurchaseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Purchase
    fields = ('id', 'created', 'updated',
    'title', 'content', 'department', 'bookTitle', 'author', 'publisher', 'price', 'isComplete',
    'purchase_comments')

class UserTransactionSerializer(serializers.ModelSerializer):
  my_sale = UserSaleSerializer(many=True)
  my_purchase = UserPurchaseSerializer(many=True)

  class Meta:
    model = User
    fields = ('my_sale', 'my_purchase')

class UserSaleInterestSerializer(serializers.ModelSerializer):
  sale = UserSaleSerializer()

  class Meta:
    model = SaleInterest
    fields = ('sale', 'created')

class UserPurchaseInterestSerializer(serializers.ModelSerializer):
  purchase = UserPurchaseSerializer()

  class Meta:
    model = PurchaseInterest
    fields = ('purchase', 'created')

class UserInterestSerializer(serializers.ModelSerializer):
  my_interest_sale = UserSaleInterestSerializer(many=True)
  my_interest_purchase = UserPurchaseInterestSerializer(many=True)

  class Meta:
    model = User
    fields = ('my_interest_sale', 'my_interest_purchase')
