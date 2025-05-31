from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views import generic
from products.forms import ProductForm
from products.models import Product


class ProductFormView(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    # success_url = reverse_lazy('add_product')
    success_url = reverse_lazy('list_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductsListView(ListView):
    # Option 1: Using ListView (Recommended - less code)
    model = Product
    template_name = 'products/list_product.html'
    context_object_name = 'products'  # This makes {{ products }} available in template
    paginate_by = 5


    def get_queryset(self):
        return Product.objects.all()  # Default manager

    # Option 2: Your current TemplateView (also works fine)
    #template_name = 'products/list_product.html'

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #products = Product.objects.all()  # Uses default manager - perfect!
        #context['products'] = products
        #return context


# View 2: Show only AVAILABLE products (using custom manager)
class AvailableProductsView(ListView):
    model = Product
    template_name = 'products/list_product.html'  # Same template!
    context_object_name = 'products'

    def get_queryset(self):
        return Product.available_products.available()  # Custom manager


# View 3: Show only IN-STOCK products (using custom manager)
class InStockProductsView(ListView):
    model = Product
    template_name = 'products/list_product.html'  # Same template!
    context_object_name = 'products'

    def get_queryset(self):
        return Product.available_products.in_stock()  # Custom manager


# View 4: Show only EXPENSIVE products (using custom manager)
class ExpensiveProductsView(ListView):
    model = Product
    template_name = 'products/list_product.html'  # Same template!
    context_object_name = 'products'

    def get_queryset(self):
        return Product.available_products.expensive()  # Custom manager
