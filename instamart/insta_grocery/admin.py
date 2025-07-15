from django.contrib import admin # type: ignore
from .models import Product # type: ignore 
# Register your models here.

admin.site.register(Product)   