from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Manufacturer, Product, Commodity

# Register your models here.
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Manufacturer)


class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 30


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer')


@admin.register(Commodity)
class CommodityAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'in_stock')
