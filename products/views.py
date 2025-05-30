from django.views import generic
from django.urls import reverse_lazy
from products.forms import ProductForm


class ProductFormView(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = '/products/add/'  # Redirect back to the same page

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)