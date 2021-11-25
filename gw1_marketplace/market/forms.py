from django import forms
from market.models import SellOrder, Category

class SellOrderForm(forms.ModelForm):

    class Meta:
        model = SellOrder
        fields = ("item", "group", "category", "total_unit", "total_price", "money_used", "description")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.none()
