from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book


class BookListView(TemplateView):
    template_name = "my_first_app/book_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch all books from the database
        books = Book.objects.all()

        # Add books to the context dictionary
        context['books'] = books

        return context


# Create your views here.
def my_view(request):
    return render(request, "my_first_app/book_list.html")

def my_view2(request, *args, **kwargs):
    print(request)
    print(args)
    print(kwargs)
    return HttpResponse(f"Hello, world! {kwargs}")