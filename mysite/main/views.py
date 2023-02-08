from django.shortcuts import render
from .models import AboutUs, HomeCars
# Create your views here.


def home(request):
    car_list = HomeCars.objects.all()
    return render(request, 'main/home.html', context={'car_list':car_list})

def about(request):
    about_list = AboutUs.objects.all()
    return render(request, 'main/about.html', context={'about_list':about_list})