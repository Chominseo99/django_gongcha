from django import forms
from .models import Topping


class ToppingUpdate(forms.ModelForm):
    class Meta:
        model = Topping
        # fields = ['__all__']
        fields = ['name', 'size', 'price']