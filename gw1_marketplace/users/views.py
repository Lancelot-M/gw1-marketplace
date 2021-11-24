from django.shortcuts import render
from market.forms import SellOrderForm

# Create your views here.
def create_order(request):
    """Add a item order"""
    form = SellOrderForm()
    return render(request, "users/create_order.html", {"form": form})