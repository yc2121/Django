from django.conf.urls import url
from . import views
   
urlpatterns = [
  url(r'^$', views.index),
  url(r'^register$', views.register),
  url(r'^login$', views.login),
  url(r'^books$', views.books),
  url(r'^books/add$', views.add_book_and_review),
  url(r'^books/(?P<id>\d+)$', views.review_details),
  url(r'^users/(?P<id>\d+)$', views.user_review),
  # url(r'^users$', views.users),
  # url(r'^farm$', views.farm),
  # url(r'^cove$', views.cove),
  # url(r'^house$', views.house),
  # url(r'^casino$', views.casino),

]