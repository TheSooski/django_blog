from django import forms
from . import models
class CreateSell(forms.ModelForm):
    class Meta:
        model = models.Sell
        fields = ['city', 'price', 'phone', 'book']