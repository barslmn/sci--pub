from django.shortcuts import render

# from django.urls import reverse_lazy
# from django.views.generic.list import ListView


def index(request):
    return render(
        request=request,
        template_name='base/index.html'
    )



## Carry to somewhere else
from publications.models import Publication
from django.views.generic.detail import DetailView

class PublicationDetailView(DetailView):

    model = Publication
    template_name='base/publication_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

