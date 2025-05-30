from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': 'Name',
            'description': 'Description',
            'price': 'Price',
            'available': 'Available',
            'stock': 'Stock',
            'photo': 'Product Photo'
        }
