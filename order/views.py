from django.db import transaction
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import FormView

from fcuser.decoraters import login_required
from fcuser.models import Fcuser
from product.models import Product
from .forms import RegisterForm
from .models import Order

@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    model = Order
    template_name = 'order.html'
    # templates/order.html에서 object_list 대신 사용할 이름
    context_object_name = 'order_list'

    def get_queryset(self):
        queryset = Order.objects.filter(fcuser__email=self.request.session.get('user'))
        return queryset

@method_decorator(login_required, name='dispatch')
class OrderRegister(FormView):
    # template_name은 상품 상세 페이지에서 보여지기 때문에 지정하지 않는다. \
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        with transaction.atomic():
            prod = Product.objects.get(pk=form.data.get('product'))
            fcuser = self.request.session.get('user')
            order = Order(
                quantity=form.data.get('quantity'),
                product=prod,
                fcuser=Fcuser.objects.get(email=fcuser)
            )
            order.save()
            prod.stock -= int(form.data.get('quantity'))
            prod.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('/product/' + str(form.data.get('product')))

    def get_form_kwargs(self, **kwargs):
        # Build the keyword arguments required to instantiate the form.
        # RegisterForm 인스턴스를 생성하기 위해 필요한 인자를 업데이트
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw
