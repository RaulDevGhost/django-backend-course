from django.urls import path
from .views import ProductFormView, ProductsListView, AvailableProductsView, InStockProductsView, ExpensiveProductsView

urlpatterns = [
    path("add/", ProductFormView.as_view(), name="add_product"),
    path("list/", ProductsListView.as_view(), name="list_product"),
    path("available/", AvailableProductsView.as_view(), name="available_products"),
    path("in-stock/", InStockProductsView.as_view(), name="in_stock_products"),
    path("expensive/", ExpensiveProductsView.as_view(), name="expensive_products"),
]
