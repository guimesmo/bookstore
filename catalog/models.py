from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=35, db_index=True)
    slug = models.SlugField(max_length=35, db_index=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, blank=True)
    sku = models.CharField(max_length=30, db_index=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
