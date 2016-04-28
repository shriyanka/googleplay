from django.conf.urls import include, url
from views import IndexView, ParseView, FetchView, ResultView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^search/$', IndexView.as_view(), name='search_item'),
    url(r'^parse/(?P<query>.+)/$', ParseView.as_view(), name='parse_item'),
    url(r'^fetch/(?P<query>.+)/$', FetchView.as_view(), name='fetch_item'),
    #url(r'^results/$', ResultView.as_view(), name='results'),
]
