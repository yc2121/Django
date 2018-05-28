from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import ImproperlyConfigured

class Main(object):
	template = ''
	context = None

	def get(self, request):
		return render(request, self.get_template())

	def get_template(self):
		if self.template == '':
			raise ImproperlyConfigured('"Template" not defined.')
		return self.template

class Home(Main, View):
	template = 'home/home.html'
	
class Profile(Main, View):
	template = 'welcome/profile.html'
