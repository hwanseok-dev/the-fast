from django.db.models import F, Q
from django.contrib import admin
from .models import Order
from django.utils.html import format_html
from django.db import transaction
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType


def refund(modelAdmin, request, queryset):
    # filter는 transaction 안에 포함되지 않는다.2
    qs = queryset.filter((~Q(status='환불')))
    ct = ContentType.objects.get_for_model(queryset.model)
    with transaction.atomic():
        for obj in qs:
            obj.product.stock += obj.quantity
            obj.product.save()
            LogEntry.objects.log_action(
                user_id=request.user.id,
                content_type_id=ct.pk,
                object_id=obj.pk,
                object_repr='주문 환불',
                action_flag=CHANGE,
                change_message='주문 환불'

            )
        qs.update(status='환불')


refund.short_description = '환불'


class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('fcuser', 'product', 'styled_status')

    actions = [
        refund
    ]

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': '주문 목록'}
        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        order = Order.objects.get(pk=object_id)
        extra_context = {'title': f'{order} 수정'}
        return super().changeform_view(request, object_id, form_url, extra_context)

    def styled_status(self, obj):
        if obj.status == '환불':
            return format_html(f'<span style="color:red">{obj.status}</span>')
        elif obj.status == '결제완료':
            return format_html(f'<span style="color:green">{obj.status}</span>')
        return obj.status

    styled_status.short_description = '상태'


admin.site.register(Order, OrderAdmin)
