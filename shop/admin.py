from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description', 'published_date', 'price']




admin.site.register(Product,ProductAdmin)