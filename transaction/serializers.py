from rest_framework import serializers

from user.models import User
from user.serializers import NicknameSerializer
from transaction.models import Sale, Purchase, SaleComment, PurchaseComment

class SaleCreateSerializer(serializers.ModelSerializer):
  sale_comments = serializers.PrimaryKeyRelatedField(many=True, queryset=SaleComment.objects.all())
  class Meta:
    model = Sale
    fields = ('id', 'user', 'created', 'updated',
    'title', 'content', 'department', 'bookTitle', 'author', 'publisher', 'price', 'isComplete',
    'sale_comments')
    read_only_fields = ('user',)

class SaleRetrieveSerializer(SaleCreateSerializer):
  user = NicknameSerializer()

class PurchaseCreateSerializer(serializers.ModelSerializer):
  purchase_comments = serializers.PrimaryKeyRelatedField(many=True, queryset=PurchaseComment.objects.all())
  class Meta:
    model = Purchase
    fields = ('id', 'user', 'created', 'updated',
    'title', 'content', 'department', 'bookTitle', 'author', 'publisher', 'price', 'isComplete',
    'purchase_comments')
    read_only_fields = ('user',)

class PurchaseRetrieveSerializer(PurchaseCreateSerializer):
  user = NicknameSerializer()

class SaleCommentCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = SaleComment
    fields = ('id', 'user', 'postId', 'created', 'updated', 'content')
    read_only_fields = ('user', 'postId',)

class SaleCommentRetrieveSerializer(SaleCommentCreateSerializer):
  user = NicknameSerializer()

class PurchaseCommentCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = PurchaseComment
    fields = ('id', 'user', 'postId', 'created', 'updated', 'content')
    read_only_fields = ('user', 'postId',)

class PurchaseCommentRetrieveSerializer(PurchaseCommentCreateSerializer):
  user = NicknameSerializer()