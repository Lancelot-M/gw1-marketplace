from django.contrib import admin
from market.models import Group, Category, SellOrder

# Register your models here.
admin.site.register(Group)
admin.site.register(Category)
admin.site.register(SellOrder)