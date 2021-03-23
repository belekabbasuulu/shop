from django.shortcuts import render
from django.views import View

from .models import Product, Image, Blog


class HomeView(View):

    def get(self,request):
        products = Product.objects.order_by('-created_at')[:15]
        return render(request, 'index.html', context={"products": products})


class CatalogView(View):
    
    def get(self, request):
        products = Product.objects.all()
        context = {
            'products' : products,
        }
        return render(request, 'shop/catalog.html', context)
        listing = Listing.objects.get(foto=foto)


class ProductDetailView(View):

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        context = {
            'product': product,
        }
        return render(request, 'shop/product_detail.html', context)


class AboutView(View):

    def get(self, request):
        return render(request, 'about_us.html')


class BlogAllView(View):

    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, 'all_blog.html', context={'blogs': blogs})

class BlogView(View):

    def get(self, request, id):
        blog = Blog.objects.get(id=id)
        return render(request, 'blog.html', context={'blog': blog})


class Womanview(View):

    def get(self, request):
        products = Product.objects.filter(gender="F")
        return render(request, 'shop/woman.html', context={"products": products})


class Manview(View):

    def get(self, request):
        products = Product.objects.filter(gender="M")
        return render(request, 'shop/man.html', context={"products": products})


class ZimaView(View):
     
     def get(self, request):
         products = Product.objects.filter(season="Зима")
         return render(request, 'shop/zima.html', context={"products": products})


class LetoView(View):
     
     def get(self, request):
         products = Product.objects.filter(season="Лето")
         return render(request, 'shop/leto.html', context={"products": products})


class DemiView(View):
     
     def get(self, request):
         products = Product.objects.filter(season="Деми")
         return render(request, 'shop/demi.html', context={"products": products})