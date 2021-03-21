from django.urls import path

from .views import (
    HomeView,
    CatalogView,
    ProductDetailView,
    AboutView,
    BlogView,
    Womanview,
    Manview,
    ZimaView,
    LetoView,
    DemiView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('catalog', CatalogView.as_view(), name='catalog'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('woman/', Womanview.as_view(), name='woman'),
    path('man/', Manview.as_view(), name='man'),
    path('zima/', ZimaView.as_view(), name='zima'),
    path('leto/', LetoView.as_view(), name='leto'),
    path('demi/', DemiView.as_view(), name='demi'),


]