from django.db import models

class Product(models.Model):
    product_code = models.UUIDField(unique=True, primary_key=True)
    name = models.CharField(max_length=64)
    product_price = models.FloatField(blank=False, null=False)
    purchase_price = models.FloatField(blank=False, null=False)
    scrapper_price = models.FloatField(blank=True, null=True)
    fee_based_price = models.FloatField(blank=True, null=True)
    stock_quantity = models.BigIntegerField(default=0)
    promotion = models.ForeignKey('Promotion', on_delete=models.CASCADE, null=True)
    enabled = models.BooleanField(default=True)

    objects = models.Manager()