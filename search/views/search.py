from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from django.http import HttpResponseRedirect
from ..forms import SearchForm
from ..models import SearchTerm
from ..utils import services


class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        form = SearchForm()
        trending = services.getTrending()
        return render(
            request, self.template_name, {
                'form': form, 'trending': trending})

    def post(self, request):
        form = SearchForm(request.POST)
        query = request.POST.get("term")
        if not query:
            return HttpResponseRedirect("/")
        if form.is_valid():
            # store the new search Term in SearchTerm Model
            term = form.save(commit=False)
            term.count += 1
            term.save()
            return HttpResponseRedirect("/fetch/%s/?new=y" % query)
        else:
            # get the cached result from SearchTerm and Apps Model
            term = SearchTerm.objects.get(term=query)
            term.count += 1
            term.save()
            return HttpResponseRedirect("/fetch/%s/?new=n" % query)


class ResultView(TemplateView):
    template_name = "results.html"
