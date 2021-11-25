from django.shortcuts import render
from market.forms import SellOrderForm, Category

# Create your views here.
def create_order(request):
    """Add a item order"""
    form = SellOrderForm()
    return render(request, "users/create_order.html", {"form": form})

def load_categories(request):
    group_id = request.GET.get('group')
    categories = Category.objects.filter(group_id=group_id).order_by('name')
    return render(request, 'hr/city_dropdown_list_options.html', {'categories': categories})