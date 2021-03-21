from django.contrib import admin

from .models import Category, Brand, Product, Image, Color, Size, Stock, Blog, Review


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Stock)
admin.site.register(Blog)
admin.site.register(Review)

