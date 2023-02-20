from django.db import models
from .validators import validate_nobb
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from django.urls import reverse


class Category(MPTTModel):
    """Category model. Will be related to the Commodity model"""
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    # def str(self):
    #     full_path = [self.name]
    #     k = self.parent
    #     while k is not None:
    #         full_path.append(k.name)
    #         k = k.parent

    #     return ' -> '.join(full_path[::-1])

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Manufacturer(models.Model):
    """ Manufactor model. Will be related to the Product model."""
    name = models.CharField(max_length=50)
    contact = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Model representing data assosiated with a spessific product."""
    name = models.CharField(max_length=100)

    manufacturer = models.ForeignKey(
        "Manufacturer",
        on_delete=models.CASCADE,
        related_name="products"
    )

    nobb = models.IntegerField(
        default=0, blank=True, validators=[validate_nobb])
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class Commodity(models.Model):
    """Model representing a product in a sales setting. This shall not be product spessific data.
    There might be scenarios were we want to sell the same product, but at different prices, e.g. outlets items.
    """
    name = models.CharField(max_length=100, blank=True)

    product = models.ForeignKey(
        "Product",
        related_name="commodities",
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        'Category',
        related_name='commodities',
        on_delete=models.CASCADE,
        null=True
    )

    price = models.FloatField()
    in_stock = models.IntegerField()
    # Planed outgoing orders for this item.
    order_out = models.IntegerField(default=0)
    # Send out an warning if the stock comes under this value.
    treshold = models.IntegerField(default=0, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.product.name
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self, *args, **kwargs):
        return reverse("commodity_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name
