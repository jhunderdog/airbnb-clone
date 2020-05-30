
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
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    room_types = models.Roomtype.objects.all()
    print(country)
    form = {"city": city, "s_room_type": room_type,  "s_country": country}
    choices = {"countries": countries, "room_types": room_types}

    return render(request, "rooms/search.html", {**form, **choices})
