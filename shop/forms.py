from django import forms


# forms.Form传递给模板时可以通过 form.as_p 或者类似的方法直接渲染成html表单
class SearchForm(forms.Form):
    search_name = forms.CharField(
        max_length=20,
        label='',
    )
