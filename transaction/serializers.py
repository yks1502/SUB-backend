from rest_framework import serializers
from user.models import User
from transaction.models import Sale
from transaction.models import Purchase

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id', 'userId', 'created', 'updated', 'title', 'content', 'department', 'bookTitle', 'author', 'publisher', 'price', 'isComplete')
        read_only_fields = ('userId',)

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('id', 'userId', 'created', 'updated', 'title', 'content', 'department', 'bookTitle', 'author', 'publisher', 'price', 'isComplete')
        read_only_fields = ('userId',)
