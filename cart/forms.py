from django import forms
from django.forms import NumberInput, widgets
from shop.models import Product, Size


class CartAddProductForm(forms.Form):

    quantity = forms.IntegerField(
        min_value=1,
        widget=NumberInput(attrs={
            'class': 'number',
            'value': 1
        }))
    # size = forms.ModelMultipleChoiceField(
    #     queryset=Size.objects.all(),
    #     widget=widgets.SelectMultiple
    # )
