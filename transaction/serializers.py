from rest_framework import serializers

from user.models import User
from user.serializers import NicknameSerializer
from transaction.models import Sale, Purchase, SaleComment, PurchaseComment

class SaleCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sale
    fields = ('id', 'user', 'created', 'updated', 'title', 'content', 'department', 'bookTitle', 'author', 'publisher', 'price', 'isComplete')
    read_only_fields = ('user',)

class SaleRetrieveSerializer(SaleCreateSerializer):
  user = NicknameSerializer()

class PurchaseCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Purchase
    fields = ('id', 'user', 'created', 'updated', 'title', 'content', 'department', 'bookTitle', 'author', 'publisher', 'price', 'isComplete')
    read_only_fields = ('user',)

class PurchaseRetrieveSerializer(PurchaseCreateSerializer):
  user = NicknameSerializer()

class SaleCommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = SaleComment
    fields = ('id', 'user', 'postId', 'created', 'updated', 'content')
    read_only_fields = ('user', 'postId',)

class PurchaseCommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = PurchaseComment
    fields = ('id', 'user', 'postId', 'created', 'updated', 'content')
    read_only_fields = ('user', 'postId',)
