from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola(request, *args, **kwargs):
    return render(request, "home.html", {})

def opcion1(request):
    return render(request, "home.html", {})
    
def opcion2(request):
    return render(request, "home.html", {})
    
def opcion3(request):
    return render(request, "home.html", {})
    