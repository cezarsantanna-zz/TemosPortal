from django import forms

class SearchPosto(forms.Form):
    posto_info = forms.CharField(max_length=100)
