from django.conf.urls import url
from . import views
   
urlpatterns = [
  url(r'^$', views.index),
  # url(r'^register/$', views.register),
  url(r'^login/$', views.login),
  url(r'^logout/$', views.logout),
  url(r'^register/$', views.register),
  url(r'^user/(?P<userID>\d+)/$', views.info),
  url(r'^user/(?P<userID>\d+)/edit/$', views.edit),
  url(r'^user/(?P<userID>\d+)/view/$', views.viewUser),
  url(r'^user/add/$', views.add),
  url(r'^addUser/$', views.addUser),
  # url(r'^wishlist_items/(?P<itemID>\d+)/view/$', views.view),
  # url(r'^wishlist_items/(?P<itemID>\d+)/remove/$', views.delete),
  # url(r'^wishlist_items/create/$', views.create),
  # url(r'^wishlist_items/new/$', views.newitem),
]