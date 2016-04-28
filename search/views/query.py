from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from ..models import SearchResultApp, Apps, SearchTerm
from ..utils import services

class ParseView(View):
	"""
	View For Parsing New Search Request and storing it in DB
	"""
	template_name = "results.html"

	def get(self,request,query):
		context = services.makeQuery(query)
		return render(request, self.template_name, {'context':context})
    		

class FetchView(View):	
	"""
	View For Fetching Existing Search Request from DB
	"""
	template_name = "results.html"

	def get(self,request,query):
		context = services.getQuery(query)
		return render(request, self.template_name, {'context':context})
