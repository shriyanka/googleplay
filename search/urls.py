from django.conf.urls import include, url
from views import IndexView, ParseView, FetchView, ResultView, DetailView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^search/$', IndexView.as_view(), name='search_item'),
    url(r'^parse/(?P<query>.+)/$', ParseView.as_view(), name='parse_item'),
    url(r'^fetch/(?P<query>.+)/$', FetchView.as_view(), name='fetch_item'),
    url(r'^detail/(?P<pk>.+)/$', DetailView.as_view(), name='app_detail'),
    #url(r'^results/$', ResultView.as_view(), name='results'),
]
