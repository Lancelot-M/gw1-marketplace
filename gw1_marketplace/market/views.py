from django.shortcuts import render
from .models import SellOrder, Category
from django.http import HttpResponse
from django.core.paginator import Paginator
from market.forms import SellOrderForm

def home(request):
    """Home page with only wallpaper"""
    return render(request, "market/searchbar.html")

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

def item(request, item_name="empty", page_nb=1):
    """Orders for an item."""
    if request.method == "GET":
        try:
            orders = SellOrder.objects.filter(item=item_name)
            if orders:
                paginator = Paginator(orders, 1)
                page = paginator.get_page(page_nb)
                return render(
                    request, "market/orders.html",
                    {
                        "page": page,
                        "searched_item": item_name,
                    }
                )
            else:
                return HttpResponse("OUPS <br/> Item non existante")
        except SellOrder.DoesNotExist:
            return HttpResponse("OUPS \nCategorie non existante")

# Create your views here.
def create_order(request):
    """Add a item order"""
    form = SellOrderForm()
    return render(request, "users/create_order.html", {"form": form})

def load_categories(request):
    group_id = request.GET.get('group')
    categories = Category.objects.filter(group_parent=group_id).order_by('name')
    return render(request, 'market/city_dropdown_list_options.html', {'categories': categories})