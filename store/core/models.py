from django.db import models
from django.utils.translation import gettext_lazy
from .validators import validate_nobb


class Category(models.Model):
    """Category model. Will be related to the Commodity model"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    """ Manufactor model. Will be related to the Product model."""
    name = models.CharField(max_length=50)
    contact = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Model representing data assosiated with a spessific product."""
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    nobb = models.IntegerField(
        default=0, blank=True, validators=[validate_nobb])

    def __str__(self):
        return self.name


class Commodity(models.Model):
    """Model representing a product in a sales setting.
    This shall not be product spessific data"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, null=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    in_stock = models.IntegerField()
    # Planed outgoing orders for this item.
    order_out = models.IntegerField(default=0)
    # Send out an warning if the stock comes under this value.
    treshold = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name
