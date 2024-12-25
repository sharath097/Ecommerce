from django.db import models
from base.models import BaseModel
# Create your models here.

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to="categories")

class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    slug = models.SlugField(unique=True, blank=True, null=True)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    price = models.IntegerField()

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    slug = models.SlugField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to="products")