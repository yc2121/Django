from django.conf.urls import url
from . import views
   
urlpatterns = [
  url(r'^$', views.index),
  url(r'^register$', views.register),
  url(r'^login$', views.login),
  url(r'^appointments$', views.dashboard),
  url(r'^show$', views.show),
  url(r'^appointments/(?P<id>\d+)$', views.update_appointment),
  # url(r'^appointment/add$', views.add_book_and_review),

]