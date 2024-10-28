from django.db import models
from django.utils import timezone
from produtex_project.models.product import Product


class Sale(models.Model):
    sale_code = models.UUIDField(unique=True, primary_key=True)
    date = models.DateField(default=timezone.now())
    products = models.ManyToManyField(Product, related_name='sales', blank=False)
    product_info = models.JSONField(defalut=dict, blank=False)
    total_price = models.FloatField(default=0.0)
    payment_info = models.JSONField(default=dict, blank=False)

    objects = models.Manager()