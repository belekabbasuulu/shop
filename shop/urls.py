from django.urls import path
from django.contrib.auth.views import LogoutView


from .views import (
    HomeView,
    CatalogView,
    ProductDetailView,
    AboutView,
    BlogAllView,
    Womanview,
    Manview,
    ZimaView,
    LetoView,
    DemiView,
    BlogView,
    MainStockView,
    StockView,
    AccountLoginView,
    AccountRegistrationView,
    ProfileView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('main-stock/', MainStockView.as_view(), name='main-stock'),
    path('stock/', StockView.as_view(), name='stock'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('about/', AboutView.as_view(), name='about'),
    path('all-blog/', BlogAllView.as_view(), name='all-blog'),
    path('blog/<int:pk>/', BlogView.as_view(), name='blog'),
    path('woman/', Womanview.as_view(), name='woman'),
    path('man/', Manview.as_view(), name='man'),
    path('zima/', ZimaView.as_view(), name='zima'),
    path('leto/', LetoView.as_view(), name='leto'),
    path('demi/', DemiView.as_view(), name='demi'),

    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', AccountRegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),



]
