from django.forms import ModelForm
from search.models import SearchTerm

class SearchForm(ModelForm):
	 class Meta:
	 	model = SearchTerm
	 	fields = ['term']
	 	exclude = ['apps','count']
