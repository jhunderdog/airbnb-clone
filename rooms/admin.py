from django.contrib import admin
from . import models


@admin.register(models.Roomtype)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    pass


# Register your models here.
