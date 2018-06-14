from django.conf.urls import url

from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
  url(r'signup$', views.user_signup),
  url(r'login$', obtain_auth_token),
  url(r'profile$', views.get_user),
  url(r'confirm_email$', views.confirm_email),
  url(r'duplicate$', views.duplicate_username),
  url(r'transactions$', views.user_transactions),
  url(r'interests$', views.user_interests),
  url(r'alarms$', views.user_alarms),
]