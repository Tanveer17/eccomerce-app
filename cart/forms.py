from django import forms

class CartForm(forms.Form):
    slug = forms.SlugField(max_length=31)
    quantity = forms.IntegerField()

