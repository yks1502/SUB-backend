from django.conf.urls import url

from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
  url(r'userlist$', views.UserList.as_view()),
  url(r'signup$', views.user_signup),
  url(r'login$', obtain_auth_token),
  url(r'profile$', views.get_user),
  url(r'confirm_email$', views.confirm_email),
]