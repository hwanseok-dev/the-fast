from django import forms
from .models import Fcuser


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        label='비밀번호'
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        label='비밀번호 확인'
    )

    def clean(self):
        cleaned_date = super().clean()
        email = cleaned_date.get('email')
        password = cleaned_date.get('password')
        re_password = cleaned_date.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('re_password', '비밀번호가 서로 다릅니다.')
            else:
                fcuser = Fcuser(
                    email=email,
                    password=password
                )
                fcuser.save()
