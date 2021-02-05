from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    # templates/product.html에서 object_list 대신 사용할 이름
    context_object_name = 'product_list'


class ProductRegister(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'
