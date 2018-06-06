from django.conf.urls import url
from . import views
   
urlpatterns = [
  url(r'^$', views.index),
  # url(r'^register/$', views.register),
  url(r'^login/$', views.login),
  url(r'^logout/$', views.logout),
  url(r'^register/$', views.register),
  url(r'^dashboard/$', views.dashboard),
  url(r'^wishlist_items/(?P<itemName>\d+)/$', views.add),
  url(r'^wishlist_items/(?P<itemid>\d+)/view/$', views.view),
  url(r'^wishlist_items/(?P<itemid>\d+)/remove/$', views.delete),
  url(r'^wishlist_items/create/$', views.create),
  url(r'^wishlist_items/new/$', views.newitem),
]