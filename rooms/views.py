
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models


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
    city = request.GET.get("city")
    print(str.capitalize(city))
    return render(request, "rooms/search.html", {"city":city})
