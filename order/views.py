from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Order
from .forms import RegisterForm


class OrderList(ListView):
    model = Order
    template_name = 'order.html'
    # templates/order.html에서 object_list 대신 사용할 이름
    context_object_name = 'order_list'

    def get_queryset(self):
        queryset = Order.objects.filter(fcuser__email=self.request.session.get('user'))
        return queryset

class OrderRegister(FormView):
    # template_name은 상품 상세 페이지에서 보여지기 때문에 지정하지 않는다. \
    form_class = RegisterForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('/product/' + str(form.product))

    def get_form_kwargs(self, **kwargs):
        # Build the keyword arguments required to instantiate the form.
        # RegisterForm 인스턴스를 생성하기 위해 필요한 인자를 업데이트
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request' : self.request
        })
        return kw