from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from user.models import User
from user.serializers import UserSerializer

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
    user.save()
    return Response(
      data = {'message': '회원가입이 성공적으로 완료되었습니다.'},
      status = status.HTTP_201_CREATED,
    )
  return Response(
    data = {'message': 'duplicate username'},
    status = status.HTTP_403_FORBIDDEN,
  )

@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def get_user(request):
  user = request.user
  if user.id is None:
    return Response(
      data = {'message': 'not authorized'},
      status = status.HTTP_403_FORBIDDEN,
    )
  user_serializer = UserSerializer(user)
  return Response(user_serializer.data)

class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer