from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = ("room", "status", "check_in", "guest", "in_progress", "is_finished")
    list_filter = ("status",)
    pass


# Register your models here.
