from django.db import models
from django.utils import timezone

# Create your models here.

class Times(models.Model):
    pres_id = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self) -> str:
        date = timezone.localtime(self.time)
        return f"({self.pk}) Presentor: {self.pres_id}, at {date.strftime('%X')}"


class Presentors(models.Model):
    name = models.CharField(max_length=300)