from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  url(r'^$', views.index),
  # url(r'^users$', views.cove),
  # url(r'^house$', views.house),
  # url(r'^casino$', views.casino),

]