from django.contrib import admin
from .models import Fcuser


class FcuserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': '사용자 목록'}
        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        fcuser = Fcuser.objects.get(pk=object_id)
        extra_context = {'title': f'{fcuser.name} 수정'}
        return super().changeform_view(request, object_id, form_url, extra_context)


admin.site.register(Fcuser, FcuserAdmin)
admin.site.site_header = "HwanSeok's BackOffice"
admin.site.index_title = "HwanSeok's BackOffice"
