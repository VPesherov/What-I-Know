from django.shortcuts import render
from demo.models import Order


# Create your views here.

def list_orders(requests):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(requests, 'orders.html', context=context)


def list_orders_filter(requests):
    orders = Order.objects.filter(positions__product__price__lte=600)
    context = {
        'orders': orders
    }
    return render(requests, 'orders.html', context=context)
