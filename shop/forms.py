from django import forms


class SearchForm(forms.Form):
    search_name = forms.CharField(
        max_length=20,
        label='',
    )
