from django.db import transaction
from django.db.models import Q

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from book.models import Book
from book.serializers import BookSerializer
from transaction.models import *
from transaction.serializers import *
from user.models import User
from user.permissions import IsOwner, IsOwnerOrReadOnly

class SaleList(generics.ListCreateAPIView):
  queryset = Sale.objects.all()
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return SaleRetrieveSerializer
    return SaleCreateSerializer

  def perform_create(self, serializer):
    data = self.request.data
    if not data.get('itemId', None):
      serializer.save(user=self.request.user)
      return
    with transaction.atomic():
      book = Book.objects.filter(itemId=data.get('itemId', None)).first()
      if book is None:
        book_data = {
          'itemId': data.get('itemId', None),
          'title': data.get('bookTitle', None),
          'author': data.get('author', None),
          'publisher': data.get('publisher', None),
          'priceStandard': data.get('priceStandard', None),
          'image': data.get('interparkImage', None),
        }
        book = BookSerializer(data=book_data)
        if not book.is_valid():
          return Response({'message': '책 정보가 올바르지 않습니다'})
        book.save()
        book = Book.objects.filter(itemId=data.get('itemId', None)).first()
      serializer.save(user=self.request.user, book=book)

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
@permission_classes((IsAuthenticated,))
def complete_sale(request, pk):
  user = request.user
  try:
    sale = Sale.objects.get(pk=pk)
  except Sale.DoesNotExist:
    return Response(
      data = {'message': '해당 상품이 존재하지 않습니다'},
      status = status.HTTP_403_FORBIDDEN,
    )
  if user != sale.user:
    return Response(
      data = {'message': '권한이 존재하지 않습니다'},
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
    data = self.request.data
    if not data.get('itemId', None):
      serializer.save(user=self.request.user)
      return
    with transaction.atomic():
      book = Book.objects.filter(itemId=data.get('itemId', None)).first()
      if book is None:
        book_data = {
          'itemId': data.get('itemId', None),
          'title': data.get('bookTitle', None),
          'author': data.get('author', None),
          'publisher': data.get('publisher', None),
          'priceStandard': data.get('priceStandard', None),
          'image': data.get('interparkImage', None),
        }
        book = BookSerializer(data=book_data)
        if not book.is_valid():
          return Response({'message': '책 정보가 올바르지 않습니다'})
        book.save()
        book = Book.objects.filter(itemId=data.get('itemId', None)).first()
      serializer.save(user=self.request.user, book=book)

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
@permission_classes((IsAuthenticated,))
def complete_purchase(request, pk):
  user = request.user
  try:
    purchase = Purchase.objects.get(pk=pk)
  except Purchase.DoesNotExist:
    return Response(
      data = {'message': '해당 상품이 존재하지 않습니다'},
      status = status.HTTP_403_FORBIDDEN,
    )
  if user != purchase.user:
    return Response(
      data = {'message': '권한이 존재하지 않습니다'},
      status = status.HTTP_403_FORBIDDEN,
    )
  purchase.isComplete = True
  purchase.save()
  return Response(
    data = {'message': '거래가 완료되었습니다'},
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
    purchase = Purchase.objects.get(pk=purchaseId)
    serializer.save(user=self.request.user, postId=purchase)

class PurchaseCommentDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = PurchaseComment.objects.all()
  permission_classes = (IsOwnerOrReadOnly,)

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return PurchaseCommentRetrieveSerializer
    return PurchaseCommentCreateSerializer

@api_view(['POST', 'DELETE'])
@permission_classes((IsAuthenticated,))
def sale_interest(request, pk):
  user = request.user
  try :
    sale = Sale.objects.get(pk=pk)
  except Sale.DoesNotExist:
    return Response(
      data = {'message': '해당 상품이 존재하지 않습니다'},
      status = status.HTTP_403_FORBIDDEN,
    )

  if request.method == 'POST':
    interest, created = SaleInterest.objects.get_or_create(user=user, sale=sale)
    if created:
      interest.save()
      return Response(
        data = {'message': '관심 판매목록에 성공적으로 추가되었습니다'},
        status = status.HTTP_200_OK,
      )
    return Response(
      data = {'message': '이미 관심 판매목록에 추가되어 있습니다'},
      status = status.HTTP_403_FORBIDDEN,
    )

  elif request.method == 'DELETE':
    try :
      interest = SaleInterest.objects.get(user=user, sale=sale)
      interest.delete()
    except SaleInterest.DoesNotExist:
      return Response(
        data = {'message': '해당 상품이 관심목록에 존재하지 않습니다'},
        status = status.HTTP_403_FORBIDDEN,
      )

class SaleInterestList(generics.ListAPIView):
  permission_classes = (permissions.IsAuthenticated,)
  serializer_class = SaleInterestSerializer

  def get_queryset(self):
    return SaleInterest.objects.filter(user=self.request.user)

@api_view(['POST', 'DELETE'])
@permission_classes((IsAuthenticated,))
def purchase_interest(request, pk):
  user = request.user
  try :
    purchase = Purchase.objects.get(pk=pk)
  except Purchase.DoesNotExist:
    return Response(
      data = {'message': '해당 상품이 존재하지 않습니다'},
      status = status.HTTP_403_FORBIDDEN,
    )

  if request.method == 'POST':
    interest, created = PurchaseInterest.objects.get_or_create(user=user, sale=sale)
    if created:
      interest.save()
      return Response(
        data = {'message': '관심 구매목록에 성공적으로 추가되었습니다'},
        status = status.HTTP_200_OK,
      )
    return Response(
      data = {'message': '이미 관심 구매목록에 추가되어 있습니다'},
      status = status.HTTP_403_FORBIDDEN,
    )

  elif request.method == 'DELETE':
    try :
      interest = PurchaseInterest.objects.get(user=user, sale=sale)
      interest.delete()
    except PurchaseInterest.DoesNotExist:
      return Response(
        data = {'message': '해당 상품이 관심목록에 존재하지 않습니다'},
        status = status.HTTP_403_FORBIDDEN,
      )

class PurchaseInterestList(generics.ListAPIView):
  permission_classes = (permissions.IsAuthenticated,)
  serializer_class = PurchaseInterestSerializer

  def get_queryset(self):
    return PurchaseInterest.objects.filter(user=self.request.user)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_sale_comments(request, pk):
  try:
    sale = Sale.objects.get(pk=pk)
  except Sale.DoesNotExist:
    return Response({'message': '해당 상품이 존재하지 않습니다'})
  queryset = SaleComment.objects.filter(postId=sale)
  serializer = SaleCommentRetrieveSerializer(queryset, many=True)
  return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_purchase_comments(request, pk):
  try:
    purchase = Purchase.objects.get(pk=pk)
  except Purchase.DoesNotExist:
    return Response({'message': '해당 상품이 존재하지 않습니다'})
  queryset = PurchaseComment.objects.filter(postId=purchase)
  serializer = PurchaseCommentRetrieveSerializer(queryset, many=True)
  return Response(serializer.data)
