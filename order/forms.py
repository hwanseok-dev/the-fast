from django import forms

'''
views.py의 OrderRegister Class에 의해서 인스턴스가 생성된다.
OrderRegister Class에서 get_form_kwargs를 통해서 request kw를 추가했기 때문에 __init__에서 request를 전달받을 수 있다.
'''


class RegisterForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    # 유저 정보는 로그인 한 사용자의 id가 입력되도록 한다.
    # 상품 상세페이지에서 상품을 클릭하기 때문에 상품 정보를 직접 입력하지 않도록 한다.
    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요.'
        },
        label='수량'
    )
    product = forms.IntegerField(
        error_messages={
            'required': '상품을 입력해주세요.'
        },
        label='상품',
        widget=forms.HiddenInput
    )

    def clean(self):
        cleaned_date = super().clean()
        quantity = cleaned_date.get('quantity')
        product = cleaned_date.get('product')
        print(f'product is {product}')
        if not (quantity and product):
            self.add_error('quantity', '수량이 없습니다.')
            self.add_error('product', '상품이 없습니다.')
