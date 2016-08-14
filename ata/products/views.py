from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Product, Group
from string import capwords

# Create your views here.

def indexView(request):
    all_groups = Group.objects.all()
    all_products = Product.objects.all()
    return render(request, "products/index.html", {
    "all_groups": all_groups,
    "all_products": all_products,
    })
    
def productDetailView(request, product_name):
    try:
        product_name = capwords(product_name.replace(" ", "_"))
        product = Product.objects.get(name = product_name)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, "products/detail.html", {"product": product})
