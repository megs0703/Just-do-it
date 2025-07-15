from django.shortcuts import render # type: ignore
from .models import Product # type: ignore
# Create your views here.

def home(request):
    prod = Product.objects.all()
    return render(request, 'insta_grocery/home.html', {"prod": prod}) 