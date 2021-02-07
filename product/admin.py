from django.contrib import admin
from django.utils.html import format_html
from django.contrib.humanize.templatetags.humanize import intcomma
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'styled_price', 'styled_stock')

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': '상품 목록'}
        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        product = Product.objects.get(pk=object_id)
        extra_context = {'title': f'{product.name} 수정'}
        return super().changeform_view(request, object_id, form_url, extra_context)

    def styled_price(self, obj):
        price = intcomma(obj.price)
        return f'{price}원'

    def styled_stock(self, obj):
        stock = obj.stock
        if stock < 10:
            stock = intcomma(stock)
            return format_html(f'<span style="color:red"><b>{stock}개</b></span>')
        elif stock > 100:
            stock = intcomma(stock)
            return format_html(f'<span style="color:green"><b>{stock}개</b></span>')
        return f'{intcomma(stock)}개'

    styled_stock.short_description = '재고'
    styled_price.short_description = '가격'


admin.site.register(Product, ProductAdmin)
