from django.contrib import admin
from django.urls import path
from fcuser.views import index, logout, RegisterView, LoginView
from product.views import ProductList, ProductRegister, ProductDetail
from order.views import OrderList, OrderRegister

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('login/', LoginView.as_view()),
    path('logout/', logout),
    path('register/', RegisterView.as_view()),
    path('product/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('product/register/', ProductRegister.as_view()),
    path('order/', OrderList.as_view()),
    path('order/register/', OrderRegister.as_view())
]
