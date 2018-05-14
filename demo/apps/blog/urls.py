from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  url(r'^$', views.index),
  url(r'^new$', views.new), 
  url(r'^create$', views.create),
  url(r'^(?P<num>\d+)$', views.show),
  url(r'^(?P<num>\d+)/edit$', views.edit),
  url(r'^(?P<num>\d+)/delete$', views.destroy),

]