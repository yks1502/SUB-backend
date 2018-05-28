from django.conf.urls import url

from book import views

urlpatterns = [
  url(r'^booklist$', views.BookList.as_view()),
  url(r'^detail/(?P<pk>[0-9]+)$', views.BookDetail.as_view()),
]