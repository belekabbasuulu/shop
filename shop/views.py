from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime
from django.db.models import Q
from django.views import View
from django.contrib import auth
from django.contrib.auth import authenticate, login

from .models import Product, Image, Blog, Stock, Category, Brand
from users.models import User
from django.contrib import messages


class ProfileView(View):

    def get(self, request):
        user = request.user
        user = User.objects.get(username=user.username)
        print(user)
        context = {
            'user': user
        }
        return render(request, 'registration/profile.html', context)


class AccountRegistrationView(View):

    def get(self, request):
        return render(request, 'registration/registration.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        image = request.POST['image']

        if password1 == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('registration')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('registration')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                    password=password1, email=email, address=address, phone_number=phone_number, image=image)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(
                        request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('registration')


class AccountLoginView(View):

    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None and User.objects.filter(username=username).exists():
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Такого пользователя нет')
            return redirect('login')


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


class ProductDetailView(View):

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        product.stock_price = product.price * (100 - product.percent) / 100
        similar_products = Product.objects.filter(
            Q(category=product.category) | Q(brand=product.brand))[:4]
        context = {
            'product': product,
            'similar_products': similar_products
        }
        return render(request, 'shop/product_detail.html', context)


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
