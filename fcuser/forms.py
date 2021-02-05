from django import forms
from django.contrib.auth.hashers import check_password, make_password
from .models import Fcuser


class LoginForm(forms.Form):
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

    def clean(self):
        # https://docs.djangoproject.com/en/3.1/ref/forms/validation/
        # After to_python(), validate(), and run_validators(),
        # returns the clean data which is then inserted into the cleaned_data dictionary of the form.
        cleaned_date = super().clean()
        email = cleaned_date.get('email')
        password = cleaned_date.get('password')

        if email and password:
            try:
                fcuser = Fcuser.objects.get(email=email)
            except Fcuser.DoesNotExist:
                self.add_error('email', '이메일이 없습니다.')

            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')
            else:
                self.email = fcuser.email


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
                    password=make_password(password)
                )
                fcuser.save()
                # TODO unique email Integrity Eror
                # except Fcuser.IntegrityError:
                #     self.add_error('email', '이미 존재하는 이메일입니다.')
