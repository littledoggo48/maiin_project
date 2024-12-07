from django.shortcuts import render, redirect
from .models import Cart, Cartitem
from django.http import JsonResponse
from django.views import View
from .models import Cart, Cartitem
from django.contrib.auth.mixins import LoginRequiredMixin
import json

# Create your views here.
def home(request):
    """ return home page """
    return render(request, 'index.html')

def contact(request):
    """ return home page """
    return render(request, 'contact.html')


def shop_details(request):
    """ view shop details """
    return render(request, 'shop-details.html')

def shop_grid(request):
    """ view shop grid"""
    return render(request, 'shop-grid.html')

class CartPageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # Get the current user's cart
        cart = Cart.objects.filter(user=request.user).first()
        return render(request, 'cart.html', {'cart': cart})

def cart(request):

    """ view cart """
    return render(request, 'shoping-cart.html')

def Delete(request, id):
    """ Deleting """
    query = Cart.objects.get(id=id)
    query.delete
    return render('app_main:cart')

class UpdateCartView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        product_name = request.POST.get('product_name')
        quantity = int(request.POST.get('quantity', 1))
        price = float(request.POST.get('price', 0))

        # Get or create a cart for the user
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Check if the item is already in the cart
        cart_item, created = Cartitem.objects.get_or_create(
            cart=cart,
            product_name=product_name,
            defaults={'quantity': quantity, 'price': price},
        )

        if not created:  # Item already exists
            cart_item.quantity += quantity
            cart_item.save()

            print(f"Product Name: {product_name}, Quantity: {quantity}, Price: {price}")


        return JsonResponse({'status': 'success', 'message': 'Cart updated successfully.'})
