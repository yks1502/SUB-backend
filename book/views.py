from rest_framework import generics

from book.models import Book
from book.serializers import BookSerializer

class BookList(generics.ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class BookDetail(generics.RetrieveDestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer