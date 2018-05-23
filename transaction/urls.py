from django.conf.urls import url

from transaction import views

urlpatterns = [
  url(r'^sales$', views.SaleList.as_view()),
  url(r'^sale/(?P<pk>[0-9]+)$', views.SaleDetail.as_view()),
  url(r'^complete_sale/(?P<pk>[0-9]+)$', views.complete_sale),
  url(r'^purchases$', views.PurchaseList.as_view()),
  url(r'^purchase/(?P<pk>[0-9]+)$', views.PurchaseDetail.as_view()),
  url(r'^complete_purchase/(?P<pk>[0-9]+)$', views.complete_purchase),
]
