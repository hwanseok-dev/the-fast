from django.contrib import admin
from django.urls import path
from fcuser.views import index, RegisterView, LoginView
from product.views import ProductList, ProductRegister
from order.views import OrderList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('product/', ProductList.as_view()),
    path('product/register/', ProductRegister.as_view()),
    path('order/', OrderList.as_view()),
]
