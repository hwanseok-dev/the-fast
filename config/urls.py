from django.contrib import admin
from django.urls import path
from fcuser.views import index, RegisterView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
]
