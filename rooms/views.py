from django.shortcuts import render
from django.views.generic import ListView
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 5
    page_kwarg = "page"
    context_object_name = "rooms"


def room_detail(request, pk):
    print(pk)
    return render(request, "rooms/detail.html")
