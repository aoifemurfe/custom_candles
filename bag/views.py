from django.shortcuts import render, redirect
from product.models import product, scents


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')
