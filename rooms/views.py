
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_countries import countries

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
    print(request.GET)
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    room_types = models.Roomtype.objects.all()
    return render(request, "rooms/search.html", {"city": city, "countries": countries, "room_types": room_types})
