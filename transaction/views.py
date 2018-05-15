from django.shortcuts import render
from transaction.models import Sale
from transaction.serializers import SaleSerializer
from user.models import User
from rest_framework.response import Response
from rest_framework import generics, permissions

class SaleList(generics.ListCreateAPIView):
  queryset = Sale.objects.all()
  serializer_class = SaleSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  
  def perform_create(self, serializer):
    serializer.save(userId=self.request.user)

class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Sale.objects.all()
  serializer_class = SaleSerializer
  permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)
