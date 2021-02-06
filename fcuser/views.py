from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm


def index(request):
    return render(request, 'index.html', {'email': request.session.get('user')})


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        # https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-editing/
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # 여기서 form은 LoginView와 연결된 LoginForm
        self.request.session['user'] = form.email
        # 아래는 form_valid의 기본 구현
        return super().form_valid(form)


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'


def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/')