import datetime
from django.db import models
from django.utils import timezone
from core import models as core_models
from . import managers


class BookedDay(core_models.TimeStampedModel):
    day = models.DateField()
    reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Booked Day"
        verbose_name_plural = "Booked Days"

    def __str__(self):
        return str(self.day)


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    status_pending = "pending"
    status_confirmed = "confirmed"
    status_canceled = "canceled"

    status_choices = (
        (status_pending, "Pending"),
        (status_confirmed, "Confirmed"),
        (status_canceled, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=status_choices, default=status_pending
    )

    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )
    check_in = models.DateField()
    check_out = models.DateField()

    objects = managers.CustomReservationManager()

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        is_finished = now > self.check_out
        if is_finished:
            BookedDay.objects.filter(reservation=self).delete()
        return is_finished

    is_finished.boolean = True

    def save(self, *args, **kwargs):
        if self.pk is None:
            start = self.check_in
            print(start)
            end = self.check_out
            print(end)
            difference = end - start
            print(difference)
            existing_booked_day = BookedDay.objects.filter(
                day__range=(start, end)
            ).exists()
            print(existing_booked_day)
            if not existing_booked_day:
                super().save(*args, **kwargs)
                print(difference.days + 1)
                for i in range(difference.days + 1):
                    day = start + datetime.timedelta(days=i)
                    print(day)
                    BookedDay.objects.create(day=day, reservation=self)
                return
        return super().save(*args, **kwargs)


# Create your models here.
