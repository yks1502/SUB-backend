from rest_framework import serializers

from user.models import User
from user.serializers import NicknameSerializer
from transaction.models import Sale, Purchase, SaleComment, PurchaseComment

class SaleCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sale
    fields = ('id', 'userId', 'created', 'updated', 'title', 'content', 'department', 'bookTitle', 'author', 'publisher', 'price', 'isComplete')
    read_only_fields = ('userId',)

class SaleRetrieveSerializer(SaleCreateSerializer):
  userId = NicknameSerializer()

class PurchaseCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Purchase
    fields = ('id', 'userId', 'created', 'updated', 'title', 'content', 'department', 'bookTitle', 'author', 'publisher', 'price', 'isComplete')
    read_only_fields = ('userId',)

class PurchaseRetrieveSerializer(PurchaseCreateSerializer):
  userId = NicknameSerializer()

class SaleCommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = SaleComment
    fields = ('id', 'userId', 'postId', 'created', 'updated', 'content')
    read_only_fields = ('userId', 'postId',)

class PurchaseCommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = PurchaseComment
    fields = ('id', 'userId', 'postId', 'created', 'updated', 'content')
    read_only_fields = ('userId', 'postId',)
