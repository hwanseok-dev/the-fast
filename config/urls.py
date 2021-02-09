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

origin_index = admin.site.index


def thefast_index(request, extra_context=None):
    # return TemplateResponse(request, 'admin/index.html', extra_context)
    extra_context = {'test':'test'}
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
