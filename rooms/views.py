
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_countries import countries

from . import models, forms

class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 5
    page_kwarg = "page"
    context_object_name = "rooms"


class RoomDetail(DetailView):
    model = models.Room
    pk_url_kwarg = 'potato'
    pass

def search(request):
    form = forms.SearchForm()
    return render(request, "rooms/search.html", {"form": form})
