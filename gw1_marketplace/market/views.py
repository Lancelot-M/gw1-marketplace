from django.shortcuts import render
from .models import SellOrder, Category
from django.http import HttpResponse
from django.core.paginator import Paginator
from market.forms import SellOrderForm

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
    if request.method == "POST":
        form = SellOrderForm(request.POST)
        if form.is_valid():
            clean_form = form.cleaned_data
            info = clean_form["description"]
            while care_space(info) != info:
                info = care_space(info)
            sell_order = SellOrder(
                item = clean_form["item"],
                group = clean_form["group"],
                category = clean_form["category"],
                total_unit = clean_form["total_unit"],
                total_price = clean_form["total_price"],
                money_used = clean_form["money_used"],
                description = info,
            )
            sell_order.save()
        else:
            print("ERRORED FORM")
            print(form.cleaned_data)
        return render(request, "users/create_order.html", {"form": form})
    else:
        form = SellOrderForm()
        return render(request, "users/create_order.html", {"form": form})


def load_categories(request):
    group_id = request.GET.get('group')
    categories = Category.objects.filter(group_parent=group_id).order_by('name')
    return render(request, 'market/city_dropdown_list_options.html', {'categories': categories})

def care_space(string):
    count = 0
    index = 0
    for char in string:
        if char == " ":
            count = 0
        if count > 19:
            spacer = string[0:index] + " " + string[index:]
            return spacer
        count += 1
        index += 1
    return string