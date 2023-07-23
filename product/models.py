from django.db import models
from django.utils.text import slugify
import uuid

# Create your models here.
def upload_to(instance, filename):
    print("filename " + filename)
    return f"images/{slugify(instance.category)}/{uuid.uuid1()} + {filename}"

class Category(models.TextChoices):
    COACHE = "Coaches"
    BED = "Beds"
    ROG = "Rugs"


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    category = models.CharField(
        max_length=255, choices=Category.choices, default=Category.COACHE)

