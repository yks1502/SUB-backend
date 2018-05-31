from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from transaction.models import Sale, Purchase, SaleComment, PurchaseComment
from transaction.serializers import *
from user.models import User
from user.permissions import IsOwner, IsOwnerOrReadOnly
from django.db.models import Q

class SaleList(generics.ListCreateAPIView):
  queryset = Sale.objects.all()
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return SaleRetrieveSerializer
    return SaleCreateSerializer

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

  def get_queryset(self):
    queryset = Sale.objects.all()
    query = self.request.query_params.get('query', None)
    if query is not None:
        queryset = queryset.filter(Q(bookTitle__icontains=query) | Q(title__icontains=query))
    return queryset


class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Sale.objects.all()
  permission_classes = (IsOwnerOrReadOnly,)

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return SaleRetrieveSerializer
    return SaleCreateSerializer

@api_view(['POST'])
@permission_classes((IsOwner,))
def complete_sale(request, pk):
  user = request.user
  sale = Sale.objects.get(pk=pk)
  if user.id is None or user.id != sale.user:
    return Response(
      data = {'message': 'not authorized'},
      status = status.HTTP_403_FORBIDDEN,
    )
  sale.isComplete = True
  sale.save()
  return Response(
    data = {'message': '거래가 완료되었습니다.'},
    status = status.HTTP_200_OK,
  )

class PurchaseList(generics.ListCreateAPIView):
  queryset = Purchase.objects.all()
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return PurchaseRetrieveSerializer
    return PurchaseCreateSerializer

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

  def get_queryset(self):
    queryset = Purchase.objects.all()
    query = self.request.query_params.get('query', None)
    if query is not None:
        queryset = queryset.filter(Q(bookTitle__icontains=query) | Q(title__icontains=query))
    return queryset

class PurchaseDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Purchase.objects.all()
  permission_classes = (IsOwnerOrReadOnly,)

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return PurchaseRetrieveSerializer
    return PurchaseCreateSerializer

@api_view(['POST'])
@permission_classes((IsOwner,))
def complete_purchase(request, pk):
  user = request.user
  purchase = Purchase.objects.get(pk=pk)
  if user.id is None or user.id != purchase.user:
    return Response(
      data = {'message': 'not authorized'},
      status = status.HTTP_403_FORBIDDEN,
    )
  purchase.isComplete = True
  purchase.save()
  return Response(
    data = {'message': '거래가 완료되었습니다.'},
    status = status.HTTP_200_OK,
  )

class SaleCommentList(generics.ListCreateAPIView):
  queryset = SaleComment.objects.all()
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return SaleCommentRetrieveSerializer
    return SaleCommentCreateSerializer

  def perform_create(self, serializer):
    saleId = self.request.data.get('saleId')
    sale = Sale.objects.get(pk=saleId)
    serializer.save(user=self.request.user, postId=sale)

class SaleCommentDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = SaleComment.objects.all()
  permission_classes = (IsOwnerOrReadOnly,)

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return SaleCommentRetrieveSerializer
    return SaleCommentCreateSerializer

class PurchaseCommentList(generics.ListCreateAPIView):
  queryset = PurchaseComment.objects.all()
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return PurchaseCommentRetrieveSerializer
    return PurchaseCommentCreateSerializer

  def perform_create(self, serializer):
    purchaseId = self.request.data.get('purchaseId')
    purchase = Sale.objects.get(pk=purchaseId)
    serializer.save(user=self.request.user, postId=puchase)

class PurchaseCommentDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = PurchaseComment.objects.all()
  permission_classes = (IsOwnerOrReadOnly,)

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return PurchaseCommentRetrieveSerializer
    return PurchaseCommentCreateSerializer
