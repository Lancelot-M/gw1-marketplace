from django import forms

class SellOrderForm(forms.Form):
    item  = forms.CharField(max_length=100)
    subcategory = forms.ChoiceField(choices=[("Swords", "EPEEEE"), ("Axes", "H")])
    total_unit = forms.IntegerField()
    total_price = forms.IntegerField()
    money_used = forms.ChoiceField(choices=[("Ectos", "Bouboule"), ("Plat", "Platine Lingo")])
    description = forms.CharField(max_length=200)
