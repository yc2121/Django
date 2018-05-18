from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

# urlpatterns = )

   
urlpatterns = [
  # patterns('crud.views',
  #  url(r'^connection/',TemplateView.as_view(template_name = 'login.html')),
  #  url(r'^login/', 'login', name = 'login')),
  url(r'^$', views.index),
  url(r'^connection$', views.login),
  url(r'^register$', views.register),
  url(r'^login$', views.login),
  # url(r'^login$', views.login),
  # url(r'^users$', views.users),
  # url(r'^users/(?P<userid>\d+)$', views.users_details),
  # url(r'^farm$', views.farm),
  # url(r'^cove$', views.cove),
  # url(r'^house$', views.house),
  # url(r'^casino$', views.casino),

]