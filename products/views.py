from django.shortcuts import render
from .models import Product

# Create your views here.
def get_product(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        return render(request, "products/product.html", {"product": product})
    except Exception as e:
        print(e)