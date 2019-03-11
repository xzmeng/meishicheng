from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,  # choices是一个combobox类型的html部件,只能从固定几个选项中选取
        coerce=int,  # 限制必须是整数
        label='数量'
    )
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
