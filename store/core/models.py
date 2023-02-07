from django.db import models
from django.utils.translation import gettext_lazy
from .validators import validate_nobb
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify


class Category(MPTTModel):
    """Category model. Will be related to the Commodity model"""
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)

    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('slug', 'parent')
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])


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

    # category = models.ForeignKey(
    #     'Category',
    #     related_name='products',
    #     on_delete=models.CASCADE
    # )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return self.slug

    def __str__(self):
        return self.name


class Commodity(models.Model):
    """Model representing a product in a sales setting.
    This shall not be product spessific data"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(
        'Category',
        related_name='products',
        on_delete=models.CASCADE,
        null=True
    )


    name = models.CharField(max_length=100)
    price = models.FloatField()
    in_stock = models.IntegerField()
    # Planed outgoing orders for this item.
    order_out = models.IntegerField(default=0)
    # Send out an warning if the stock comes under this value.
    treshold = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name
