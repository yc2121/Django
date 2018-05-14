from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  url(r'^$', views.index),
  url(r'^farm$', views.farm),
  url(r'^cove$', views.cove),
  url(r'^house$', views.house),
  url(r'^casino$', views.casino),

]