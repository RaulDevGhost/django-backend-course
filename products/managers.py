from django.db import models


class ProductManager(models.Manager):
    def available(self):
        return self.filter(available=True)

    def in_stock(self):
        return self.filter(stock__gt=0)

    def expensive(self):
        return self.filter(price__gte=100)

    def available_and_in_stock(self):
        return self.filter(available=True, stock__gt=0)