from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_product, name="get_product"),
]