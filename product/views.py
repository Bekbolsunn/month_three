from django.shortcuts import render
from . import models, forms


def home_page(requests):
    products = models.Product.objects.filter().order_by('-id')
    return render(requests, 'home_page.html', {'product': products})

