from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    description = models.TextField(max_length=300, blank=True, verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True, verbose_name="Available")
    stock = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Product Photo")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']