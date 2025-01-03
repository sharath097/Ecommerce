from django.shortcuts import render

# Create your views here.
def get_product(request):
    return render(request, "products/product.html")