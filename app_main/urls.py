from django.urls import path
from . import views
from .views import UpdateCartView
from .views import CartPageView

app_name = 'app_main'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name = 'contact'),
    path('shop_details/', views.shop_details, name='shop_details'),
    path('shop_grid/', views.shop_grid, name='shop_grid'),
    path('cart/', views.cart, name='cart'),
    path('update_cart/', UpdateCartView.as_view(), name='update_cart'),
    path('cart_page/', CartPageView.as_view(), name='cart_page')
]   