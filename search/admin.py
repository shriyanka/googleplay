from django.contrib import admin
from search.models import SearchTerm, Apps, SearchResultApp


class SearchTermAdmin(admin.ModelAdmin):
    list_display = ('term', 'count')


class AppsAdmin(admin.ModelAdmin):
    # Good practice, I like this. :)
    model = Apps
    list_display = ('app_id', 'app_name', 'developer_name')


class SearchResultAppAdmin(admin.ModelAdmin):
    model = SearchResultApp
    list_display = ('term', 'app')

admin.site.register(SearchTerm, SearchTermAdmin)
admin.site.register(SearchResultApp, SearchResultAppAdmin)
admin.site.register(Apps, AppsAdmin)
