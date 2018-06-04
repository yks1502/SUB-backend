from rest_framework import serializers

from user.models import User
from book.models import Book
from user.serializers import NicknameSerializer
from book.serializers import BookSerializer
from transaction.models import *

class SaleCreateSerializer(serializers.ModelSerializer):
  image = serializers.ImageField(use_url=True, required=False)

  class Meta:
    model = Sale
    fields = ('id', 'user', 'created', 'updated',
    'title', 'content', 'department', 'bookTitle', 'author', 'publisher', 'price', 'isComplete', 'image',
    'contact', 'sale_comments', 'book')
    read_only_fields = ('user', 'sale_comments')

class SaleRetrieveSerializer(SaleCreateSerializer):
  sale_comments = serializers.PrimaryKeyRelatedField(many=True, queryset=SaleComment.objects.all())
  user = NicknameSerializer()
  book = BookSerializer()

class PurchaseCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Purchase
    fields = ('id', 'user', 'created', 'updated',
    'title', 'content', 'department', 'bookTitle', 'author', 'publisher', 'price', 'isComplete',
    'contact', 'purchase_comments', 'book')
    read_only_fields = ('user', 'purchase_comments')

class PurchaseRetrieveSerializer(PurchaseCreateSerializer):
  user = NicknameSerializer()
  purchase_comments = serializers.PrimaryKeyRelatedField(many=True, queryset=PurchaseComment.objects.all())
  book = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=Book.objects.all())

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

class SaleInterestSerializer(serializers.ModelSerializer):
  class Meta:
    model = SaleInterest
    fields = ('id', 'user', 'sale')
    read_only_fields = ('user', 'sale',)

class PurchaseInterestSerializer(serializers.ModelSerializer):
  class Meta:
    model = PurchaseInterest
    fields = ('id', 'user', 'purchase')
    read_only_fields = ('user', 'purchase',)
