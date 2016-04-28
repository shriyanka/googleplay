from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from ..forms import SearchForm
from ..models import SearchResultApp, Apps, SearchTerm

class IndexView(View):
    template_name = "index.html"
    
    def get(self,request):
    	form = SearchForm()    	
    	return render(request, 'index.html', {'form': form})

    def post(self,request):
    	form = SearchForm(request.POST)
    	query = request.POST.get("term")
    	if form.is_valid():
    		# store the new search Term in SearchTerm Model
    		term = form.save(commit=False)
    		term.count+=1
    		term.save()
    		return HttpResponseRedirect("/parse/%s/"%query)
    	else:
    		#get the cached result from SearchTerm and Apps Model
    		term = SearchTerm.objects.get(term=query)
    		term.count+=1
    		term.save()
    		return HttpResponseRedirect("/fetch/%s/"%query)

class ResultView(TemplateView):
	template_name = "results.html"