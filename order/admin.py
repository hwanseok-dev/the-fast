import datetime
from django.contrib import admin
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from django.db.models import Q
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.html import format_html

from .models import Order


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
    list_display = (
        'id',
        'fcuser',
        'product',
        'styled_status',
        'action_btn_refund')
    change_list_template = 'admin/order_change_list.html'

    actions = [
        refund
    ]

    def action_btn_refund(self, obj):
        if obj.status != "환불":
            return format_html(
                f'<input type="button" value="환불" onclick="order_refund_submit({obj.id})" class="btn '
                'btn-primary btn-sm">')

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': '주문 목록'}

        if request.method == 'POST':
            obj_id = request.POST.get('obj_id')
            if obj_id:
                qs = Order.objects.filter(pk=obj_id)
                ct = ContentType.objects.get_for_model(qs.model)
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

        return super().changelist_view(request, extra_context)

    def changeform_view(
            self,
            request,
            object_id=None,
            form_url='',
            extra_context=None):
        order = Order.objects.get(pk=object_id)
        extra_context = {'title': f'{order} 수정'}
        return super().changeform_view(request, object_id, form_url, extra_context)

    def styled_status(self, obj):
        if obj.status == '환불':
            return format_html(f'<span style="color:red">{obj.status}</span>')
        elif obj.status == '결제완료':
            return format_html(
                f'<span style="color:green">{obj.status}</span>')
        return obj.status

    def get_urls(self):
        urls = super().get_urls()
        date_urls = [
            path('date_view/', self.date_view)
        ]
        return date_urls + urls

    def date_view(self, request):
        week_date = datetime.datetime.now() - datetime.timedelta(days=7)
        week_data = Order.objects.filter(register_date__gte=week_date)
        data = Order.objects.filter(register_date__lt=week_date)
        context = dict(
            self.admin_site.each_context(request),
            week_data=week_data,
            data=data
        )

        return TemplateResponse(request, 'admin/order_date_view.html', context)

    styled_status.short_description = '상태'


admin.site.register(Order, OrderAdmin)
