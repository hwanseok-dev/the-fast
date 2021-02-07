from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from rest_framework import generics, mixins
from django.utils.decorators import method_decorator
from fcuser.decoraters import admin_required
from order.forms import RegisterForm as OrderRegisterForm
from .forms import RegisterForm
from .models import Product
from .serializers import ProductSerializer

class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    # 데이터의 검증을 위해 serializer 등록 필수
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    # 데이터의 검증을 위해 serializer 등록 필수
    serializer_class = ProductSerializer

    # detail에 대한 API이지만 전체 queryset에서 전달받은 pk와 매칭되는 object만 api로 제공해준다.
    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    # templates/product.html에서 object_list 대신 사용할 이름
    context_object_name = 'product_list'

@method_decorator(admin_required, name='dispatch')
class ProductRegister(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        product = Product(
            name=form.data.get('name'),
            price=form.data.get('price'),
            description=form.data.get('description'),
            stock=form.data.get('stock')
        )
        product.save()
        return super().form_valid(form)

class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        # 화면에 보여질 데이터를 dictionary로 리턴
        context = super().get_context_data(**kwargs)
        # 화면에 OrderForm을 전달하기 위해 등록한다.
        ## View Class이기 때문에 self.request가 존재한다.
        ## OrderForm에 self.request를 전달하는 것은 order/RegisterForm에서 request를 사용해서 session을 사용하기 위함
        context['form'] = OrderRegisterForm(self.request)
        return context
