from django.forms import ModelForm
from .models import Order, Customer, Product


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'





