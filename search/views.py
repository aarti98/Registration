from django.shortcuts import render
from uploadfiles.models import Document
from django.views.generic import ListView
# Create your views here.

class SearchView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args,**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')

        if query is not None:
            return Document.objects.search(query)

        return Document.objects.none()