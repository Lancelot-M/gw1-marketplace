from django.shortcuts import render
from .models import SellOrder, Category
from django.http import HttpResponse
from django.core.paginator import Paginator

def home(request):
    """Home page with only wallpaper"""
    return render(request, "market/home.html")

def category(request, category_name, page_nb=1):
    """Orders about a category"""
    if request.method == "GET":
        try:
            items = SellOrder.objects.filter(category__name=category_name)
            paginator = Paginator(items, 1)
            page = paginator.get_page(page_nb)
            return render(
                request, "market/orders.html",
                {
                    "page": page,
                    "category_selected": category_name
                }
            )
        except SellOrder.DoesNotExist:
            return HttpResponse("OUPS \nCategorie non existante")

def item(request, item_name, page_nb=1):
    """Orders for an item."""
    if request.method == "GET":
        try:
            orders = SellOrder.objects.filter(item=item_name)
            paginator = Paginator(orders, 25)
            page = paginator.get_page(page_nb)
            return render(
                request, "market/orders.html",
                {
                    "page": page,
                }
            )
        except SellOrder.DoesNotExist:
            return HttpResponse("OUPS \nCategorie non existante")