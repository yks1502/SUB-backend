from rest_framework import serializers

from book.models import Book

class BookSerializer(serializers.ModelSerializer):
  image = serializers.ImageField(use_url=True)
  
  class Meta:
    model = Book
    fields = ('itemId', 'title', 'publisher', 'author', 'priceStandard', 'image')
