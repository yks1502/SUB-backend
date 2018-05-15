from django.conf.urls import url
from transaction import views

urlpatterns = [
  url(r'^sales$', views.SaleList.as_view()),
  url(r'^sale/(?P<pk>[0-9]+)$', views.SaleDetail.as_view()),
]