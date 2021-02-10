from django.contrib import admin
from django.urls import path, include, re_path
from fcuser.views import index, logout, RegisterView, LoginView
from product.views import (
    ProductList, ProductRegister, ProductDetail,
    ProductListAPI, ProductDetailAPI
)
from order.views import OrderList, OrderRegister
from django.views.generic import TemplateView
from django.template.response import TemplateResponse
import datetime
from order.models import Order
from .functions import get_exchange

origin_index = admin.site.index


def thefast_index(request, extra_context=None):
    # return TemplateResponse(request, 'admin/index.html', extra_context)
    base_date = datetime.datetime.now() - datetime.timedelta(days=7)
    order_data = {}
    for i in range(7):
        target_dttm = base_date + datetime.timedelta(days=i)
        date_key = target_dttm.strftime('%Y-%m-%d')
        target_date = datetime.date(target_dttm.year, target_dttm.month, target_dttm.day)
        order_cnt = Order.objects.filter(register_date__date=target_date).count()
        order_data[date_key] = order_cnt
    extra_context = {
        'orders': order_data,
        'exchange': get_exchange()
    }
    return origin_index(request, extra_context)


admin.site.index = thefast_index

urlpatterns = [
    re_path(r'^admin/manual/$', TemplateView.as_view(
        template_name='admin/manual.html',
        extra_context={
            'title': '메뉴얼',
            'site_title': "HwanSeok's BackOffice",
            'site_header': "HwanSeok's BackOffice"
        }
    )),
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('', index),
    path('login/', LoginView.as_view()),
    path('logout/', logout),
    path('register/', RegisterView.as_view()),
    path('product/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('product/register/', ProductRegister.as_view()),
    path('order/', OrderList.as_view()),
    path('order/register/', OrderRegister.as_view()),
    path('api/product/', ProductListAPI.as_view()),
    path('api/product/<int:pk>', ProductDetailAPI.as_view())
]
