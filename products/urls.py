from django.urls import path
from .views import ProductFormView, ProductsListView

urlpatterns = [
    path("add/", ProductFormView.as_view(), name="add_product"),
    path("list/", ProductsListView.as_view(), name="list_product"),
]
