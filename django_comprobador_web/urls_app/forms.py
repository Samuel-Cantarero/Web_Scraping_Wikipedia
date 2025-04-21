from django import forms

class UrlForm(forms.Form):
    url = forms.URLField(label='Introduce una web', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'https://ejemplo.com'}))
