from django.db import models
from django.utils import timezone


class Promotion(models.Model):
    promotion_code = models.UUIDField(primary_key=True, unique=True)
    percentage = models.FloatField(default=0.1)
    start_date = models.DateField(default=timezone.now())
    end_date = models.DateField(blank=True, null=True)
    enabled = models.BooleanField(default=True)

    objects = models.Manager()
    