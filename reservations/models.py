from django.db import models
from core import models as core_models


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    status_pending = "pending"
    status_confirmed = "confirmed"
    status_canceled = "canceled"

    status_choices = (
        (status_pending, "pending"),
        (status_confirmed, "confirmed"),
        (status_canceled, "canceled"),
    )

    status = models.CharField(
        max_length=12, choices=status_choices, default=status_pending
    )

    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.room} - {self.check_in}"


# Create your models here.
