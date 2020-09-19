from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import OrderForm

# Create your views here.
def home(request):
    last_5_orders = Order.objects.all().order_by('-date_created')[:5]
    customers = Customer.objects.all()
    total_orders = Order.objects.all()
    total_orders_delivered = total_orders.filter(status='Delivered').count()
    total_orders_pending = total_orders.filter(status='Pending').count()
    context = {
        'last_5_orders': last_5_orders,
        'customers': customers,
        'total_orders': total_orders.count(),
        'total_orders_delivered': total_orders_delivered,
        'total_orders_pending': total_orders_pending
    }
    return render(request, 'accounts/dashboard.html', context)


def customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = customer.order_set.all()
    total_orders = orders.count()
    context = {'customer': customer, 'orders': orders, 'total_orders': total_orders}
    return render(request, 'accounts/customer.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {
        'products': products
    })


def create_order(request):
    form = OrderForm()
    context = {'form': form}
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'accounts/order_form.html', context)


def update_order(request, order_id):
    order = Order.objects.get(id=order_id)
    # To prefill form with order data use keyword instance
    form = OrderForm(instance=order)
    context = {'form': form}
    if request.POST:
        form = OrderForm(request.POST, instance=order)  # !!!!! You must include the instance, otherwise you add another order
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'accounts/order_form.html', context)


def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    context = {'item': order}
    if request.POST:
        order.delete()
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'accounts/delete.html', context)