from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from ..models import SearchResultApp, Apps, SearchTerm
from ..utils import services, constants
from ..forms import SearchForm

class ParseView(View):
	"""
	View For Parsing New Search Request and storing it in DB
	"""
	template_name = "results.html"

	def get(self,request,query):
		form = SearchForm()
		context = services.makeQuery(query)
		return render(request, self.template_name, {'form': form,'context':context})
    		

class FetchView(View):	
	"""
	View For Fetching Existing Search Request from DB
	"""
	template_name = "results.html"

	def get(self,request,query):
		form = SearchForm()
		context = services.getQuery(query)
		return render(request, self.template_name, {'form': form,'context':context,'term':query})


class DetailView(View):
	"""
	View for showing the details of particular app
	"""
	template_name = "details.html"

	def get(self,request,pk):
		term = request.GET.get('term')
		try:
			app = Apps.objects.get(id=int(pk))
		except:
			# if the details has been removed or wrong id entered
			app = constants.DETAILS_NOT_FOUND
		
		return render(request, self.template_name, {'context':app,'term':term})
