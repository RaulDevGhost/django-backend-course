from django.db import models
from products.managers import ProductManager

def product_image_path(instance, filename):
    # Upload to MEDIA_ROOT/products/product_name/filename
    return f'products/{instance.name}/{filename}'

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    description = models.TextField(max_length=300, blank=True, verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True, verbose_name="Available")
    stock = models.PositiveIntegerField()
    photo = models.ImageField(
        upload_to=product_image_path,  # Custom upload path
        null=True,
        blank=True,
        verbose_name="Product Photo"
    )

    # Managers
    objects = models.Manager()  # Default manager
    available_products = ProductManager()  # Custom manager from managers.py
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']