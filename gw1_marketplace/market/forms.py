from django import forms
from market.models import SellOrder, Category

class SellOrderForm(forms.ModelForm):

    class Meta:
        model = SellOrder
        fields = ("item", "group", "category", "total_unit", "total_price", "money_used", "description")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.none()
        self.fields['description'].required = False

        if 'group' in self.data:
            try:
                group_id = int(self.data.get('group'))
                self.fields['category'].queryset = Category.objects.filter(group_parent=group_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['category'].queryset = self.instance.group.category_set.order_by('name')