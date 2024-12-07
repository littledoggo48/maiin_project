from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    """ Cart """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Cart {self.id} for {self.user}'

class Cartitem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_price(self):
        return self.quantity * self.price
    
    def __str__(self):
        return f'{self.quantity} of {self.product_name}'
