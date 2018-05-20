from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^appointments', views.create, name='create'),
    url(r'^search', views.search, name='search'),


]
