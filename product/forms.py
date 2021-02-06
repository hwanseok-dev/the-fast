from django import forms
from .models import Product


class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required': '상품명을 입력해주세요.'
        },
        max_length=64, label='상품명'
    )
    price = forms.IntegerField(
        error_messages={
            'required': '상품가격을 입력해주세요.'
        },
        label='상품가격'
    )
    description = forms.CharField(
        error_messages={
            'required': '상품설명을 입력해주세요.'
        },
        label='상품설명'
    )
    stock = forms.IntegerField(
        error_messages={
            'required': '재고를 입력해주세요.'
        },
        label='재고'
    )

    def clean(self):
        # https://docs.djangoproject.com/en/3.1/ref/forms/validation/
        # After to_python(), validate(), and run_validators(),
        # returns the clean data which is then inserted into the cleaned_data dictionary of the form.
        cleaned_date = super().clean()

        name = cleaned_date.get('name')
        price = cleaned_date.get('price')
        description = cleaned_date.get('description')
        stock = cleaned_date.get('stock')

        if not(name and price and description and stock):
            self.add_error('name','상품 이름을 입력해주세요.')
            self.add_error('price','상품 가격을 입력해주세요.')
            self.add_error('description','상품설명을 입력해주세요.')
            self.add_error('stock','재고를 입력해주세요')
