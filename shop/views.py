from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()[0:2]
    return render(request, 'index.html', {'products': products})

def about(request):
    return render(request, 'about.html')

def video(request):
    return render(request, 'video.html')

def contact(request):
    return render(request, 'contact.html')

def remot(request):
    return render(request, 'remot.html')

def product(request):
    prods = Product.objects.all()
    return render(request,'product.html', {'products': prods})

def get_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': Product.objects.get(id=id)})









