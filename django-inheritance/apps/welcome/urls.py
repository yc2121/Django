from django.conf.urls import patterns, url
from apps.welcome.views import Home
urlpatterns = patterns('',
	url(r'^$', Home.as_view()),
)