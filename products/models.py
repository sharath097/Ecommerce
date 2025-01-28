from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
# Create your models here.

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    category_image = models.ImageField(upload_to="categories/images")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name

class ColorVariant(BaseModel):
    color_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.color_name

class SizeVariant(BaseModel):
    size_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.size_name

class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    slug = models.SlugField(unique=True, blank=True, null=True)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    price = models.IntegerField()
    color_variant = models.ManyToManyField(ColorVariant, blank=True)
    size_variant = models.ManyToManyField(SizeVariant, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name

    def product_price_by_size(self, size):
        return self.price + SizeVariant.objects.get(size_name = size).price

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    slug = models.SlugField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to="products/images")