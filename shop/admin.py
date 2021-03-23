from django.contrib import admin
from django import forms

from .models import Category, Brand, Product, Image, Color, Size, Stock, Blog, Review

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BlogAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Blog
        fields = '__all__'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'created_at')
    list_display_links = ('title',)
    list_filter = ('title', 'id', 'created_at')
    search_fields = ('id', 'title')
    form = BlogAdminForm


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Stock)
admin.site.register(Review)

