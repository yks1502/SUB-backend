from django.shortcuts import render
from transaction.models import Sale
from transaction.serializers import SaleSerializer
from user.models import User
from user.permissions import IsOwner
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes

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

@permission_classes((IsOwner,))
@api_view(['POST'])
def complete_sale(request, pk):
  user = request.user
  if user.id is None:
    return Response(
      data = {'message': 'not authorized'},
      status = status.HTTP_403_FORBIDDEN,
    )

  sale = Sale.objects.get(pk=pk)

  sale.isComplete = True
  sale.save()
  return Response(
    data = {'message': '거래가 완료되었습니다.'},
    status = status.HTTP_200_OK,
  )