from django.conf.urls import url
from . import views
   
urlpatterns = [
  url(r'^$', views.index),
  # url(r'^register/$', views.register),
  url(r'^login/$', views.login),
  url(r'^logout/$', views.logout),
  url(r'^register/$', views.register),
  url(r'^package/$', views.package),
  url(r'^user/(?P<userid>\d+)/$', views.userpage),
  # url(r'^package/(?P<id>\d+)/create/$', views.create),
  url(r'^package/(?P<packageID>\d+)/add/$', views.add),
  # url(r'^package/(?P<id>\d+)/update/$', views.update),
  url(r'^package/(?P<packageID>\d+)/delete/$', views.delete),

]