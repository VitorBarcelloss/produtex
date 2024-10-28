from django.db import models

class ReportConfig(models.Model):
    enable_forecasting = models.BooleanField(default=True)
    base_period = models.IntegerField(verbose_name='base period in months', default=3)
    fees = models.JSONField(default=dict)
    enable_promotion_analysis = models.BooleanField(default=True)

    objects = models.Manager()