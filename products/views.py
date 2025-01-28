from django.shortcuts import render
from .models import Product
from django.http import JsonResponse

# Create your views here.
def get_product(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Check if the request is AJAX
            size = request.GET.get('size')
            price = product.product_price_by_size(size)
            return JsonResponse({"price": price})
        context = {
            "product": product
        }
        return render(request, "products/product.html", context=context)
    except Exception as e:
        print(e)
