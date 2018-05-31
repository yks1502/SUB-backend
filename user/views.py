from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from user.models import User
from user.serializers import *

@api_view(['POST'])
def user_signup(request):
  def is_valid_email(email):
    try:
      validate_email(email)
      email_id, email_domain = email.split("@")
      if email_domain != 'snu.ac.kr':
        return False
      return True
    except ValidationError:
      return False

  data = request.data
  username = data.get('username', '')
  password = data.get('password', '')
  email = data.get('email', '')
  nickname = data.get('nickname', '')

  if len(username) < 6:
    return Response(
      data = {'message': 'invalid username, must be at least 6 charactors long'},
      status = status.HTTP_403_FORBIDDEN,
    )

  if not is_valid_email(email):
    return Response(
      data = {'message': 'invalid email'},
      status = status.HTTP_403_FORBIDDEN,
    )

  user, created = User.objects.get_or_create(username=username)

  if created:
    user.email = email
    user.set_password(password)
    user.nickname = nickname
    token = Token.objects.create(user=user)
    user.confirmationToken = token.key
    user.save()
    return Response(
      data = {'message': '회원가입이 성공적으로 완료되었습니다.'},
      status = status.HTTP_201_CREATED,
    )
  return Response(
    data = {'message': 'duplicate username'},
    status = status.HTTP_403_FORBIDDEN,
  )

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_user(request):
  user_serializer = UserSerializer(request.user)
  return Response(user_serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def confirm_email(request):
  user = request.user
  token = request.data.get('token', '')
  if user.confirmationToken != token:
    return Response(
      data = {'message': '이메일 인증에 실패하였습니다'},
      status = status.HTTP_403_FORBIDDEN,
    )
  user.isConfirmed = True
  return Response(
    data = {'message': '이메일이 인증되었습니다'},
    status = status.HTTP_200_OK,
  )

@api_view(['POST'])
def duplicate_username(request):
  username = request.data
  if User.objects.filter(username=username):
    return Response(
      data = {'message': '중복되는 아이디가 존재합니다'},
      status = status.HTTP_403_FORBIDDEN,
    )
  return Response(
    data = {'message': '사용할 수 있는 아이디입니다'},
    status = status.HTTP_200_OK,
  )

class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def user_transactions(request):
  user_transaction_serializer = UserTransactionSerializer(request.user)
  return Response(user_transaction_serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def user_interests(request):
  user_interest_serializer = UserInterestSerializer(request.user)
  return Response(user_interest_serializer.data)