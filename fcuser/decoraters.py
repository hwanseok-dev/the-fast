from django.shortcuts import redirect
from .models import Fcuser

def login_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')
        return function(request, *args, **kwargs)

    return wrap

# @login_required 여기다가도 decorater 가능!
def admin_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')

        user = Fcuser.objects.get(email=user)
        if user.level != 'admin':
            return redirect('/')
        return function(request, *args, **kwargs)

    return wrap
