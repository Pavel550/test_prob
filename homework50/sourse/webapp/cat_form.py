from django import forms


class CatForm(forms.Form):
    name = forms.CharField(label='Name', max_length=20)