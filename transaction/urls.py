from django.conf.urls import url

from transaction import views

urlpatterns = [
  url(r'^sales$', views.SaleList.as_view()),
  url(r'^sale/(?P<pk>[0-9]+)$', views.SaleDetail.as_view()),
  url(r'^sale/comments$', views.SaleCommentList.as_view()),
  url(r'^sale/comment/(?P<pk>[0-9]+)$', views.SaleCommentDetail.as_view()),
  url(r'^sale/(?P<pk>[0-9]+)/complete$', views.complete_sale),
  url(r'^sale/(?P<pk>[0-9]+)/interest$', views.sale_interest),
  url(r'^sale/interests$', views.SaleInterestList.as_view()),

  url(r'^purchases$', views.PurchaseList.as_view()),
  url(r'^purchase/(?P<pk>[0-9]+)$', views.PurchaseDetail.as_view()),
  url(r'^purchase/comments$', views.PurchaseCommentList.as_view()),
  url(r'^purchase/comment/(?P<pk>[0-9]+)$', views.PurchaseCommentDetail.as_view()),
  url(r'^purchase/(?P<pk>[0-9]+)/complete$', views.complete_purchase),
  url(r'^purchase/(?P<pk>[0-9]+)/interest$', views.purchase_interest),
  url(r'^purchase/interests$', views.PurchaseInterestList.as_view()),
]
