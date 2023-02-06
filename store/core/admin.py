from django.contrib import admin
from .models import Genre, Manufacture, Product, Commodity

# Register your models here.
admin.site.register(Genre)
admin.site.register(Manufacture)
admin.site.register(Product)
admin.site.register(Commodity)
