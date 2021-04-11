from django.shortcuts import render
from django.views import View
from datetime import datetime
from .models import Product, Image, Blog, Stock, Category, Brand


class HomeView(View):

    def get(self, request):
        products = Product.objects.order_by('-created_at')[:15]
        return render(request, 'index.html', context={"products": products})


class CatalogView(View):

    def get(self, request):
        products = Product.objects.all()
        for i in products:
            i.stock_price = i.price * (100 - i.percent) / 100
        categories = Category.objects.all()
        brands = Brand.objects.all()
        title_of_page = "КАТАЛОГ"
        context = {
            'products': products,
            'categories': categories,
            'brands': brands,
            'title_of_page': title_of_page,

        }
        return render(request, 'shop/catalog.html', context)


class MainStockView(View):

    def get(self, request):
        stocks = Stock.objects.all()
        context = {
            'stocks': stocks,
        }
        return render(request, 'shop/main_stock.html', context)


class StockView(View):

    def get(self, request):
        products = Product.objects.filter(percent__gt=0)
        for i in products:
            i.stock_price = i.price * (100 - i.percent) / 100
        context = {
            'products': products,
        }
        return render(request, 'shop/stock.html', context)


class ProductDetailView(View):

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        product.stock_price = product.price * (100 - product.percent) / 100
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

    def get(self, request, pk):
        blog = Blog.objects.get(id=pk)
        return render(request, 'blog.html', context={'blog': blog})


class Womanview(View):

    def get(self, request):
        products = Product.objects.filter(gender="F")
        categories = Category.objects.all()
        title_of_page = "ЖЕНСКАЯ ОБУВЬ"
        context = {
            "categories": categories,
            "products": products,
            'title_of_page': title_of_page
        }
        return render(request, 'shop/catalog.html', context)


class Manview(View):

    def get(self, request):
        products = Product.objects.filter(gender="M")
        categories = Category.objects.all()
        title_of_page = "МУЖСКАЯ ОБУВЬ"
        context = {
            "categories": categories,
            "products": products,
            'title_of_page': title_of_page
        }
        return render(request, 'shop/catalog.html', context)


class ZimaView(View):

    def get(self, request):
        products = Product.objects.filter(season="Зима")
        categories = Category.objects.all()
        title_of_page = "ЗИМНЯЯ ОБУВЬ"
        context = {
            "categories": categories,
            "products": products,
            'title_of_page': title_of_page
        }
        return render(request, 'shop/catalog.html', context)


class LetoView(View):

    def get(self, request):
        products = Product.objects.filter(season="Лето")
        categories = Category.objects.all()
        title_of_page = "ЛЕТНЯЯ ОБУВЬ"
        context = {
            "categories": categories,
            "products": products,
            'title_of_page': title_of_page
        }
        return render(request, 'shop/catalog.html', context)


class DemiView(View):

    def get(self, request):
        products = Product.objects.filter(season="Деми")
        categories = Category.objects.all()
        title_of_page = "ДЕМИ СЕЗОННАЯ ОБУВЬ"
        context = {
            "categories": categories,
            "products": products,
            'title_of_page': title_of_page
        }
        return render(request, 'shop/catalog.html', context)
