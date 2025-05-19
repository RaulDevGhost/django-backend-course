from django.shortcuts import render

# Create your views here.
def my_view(request):
    return render(request, "my_first_app/car_list.html")