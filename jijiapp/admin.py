from django.contrib import admin
from .models import product,cart,region,category

# Register your models here.
admin.site.register(product)
admin.site.register(cart)
admin.site.register(region)
admin.site.register(category)
