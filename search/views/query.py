from django.shortcuts import render
from django.views.generic import View
from ..models import Apps
from ..utils import services, constants
from ..forms import SearchForm


class FetchView(View):
    """
    View For Fetching Existing Search Request from DB or Creating a new one
    """
    template_name = "results.html"

    def get(self, request, query):
        form = SearchForm()
        trending = services.getTrending()

        newSearchTerm = request.GET.get("new")
        if newSearchTerm == constants.NEW:
            print("New Search Term")
            context = services.makeQuery(query)
        else:
            print("Existing Search Term")
            context = services.getQuery(query)

        return render(
            request, self.template_name, {
                'form': form, 'context': context, 'term': query, 'trending': trending})


class DetailView(View):
    """
    View for showing the details of particular app
    """
    template_name = "details.html"

    def get(self, request, pk):
        term = request.GET.get('term')
        trending = services.getTrending()
        try:
            app = Apps.objects.get(app_id=pk)
        except:
            # if the details has been removed or wrong id entered
            app = constants.DETAILS_NOT_FOUND

        return render(
            request, self.template_name, {
                'context': app, 'term': term, 'trending': trending})
