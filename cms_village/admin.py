from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from cms_village.models import *
from cms_village.forms import *


class AccommodationTagInline(admin.TabularInline):
    model = AccommodationTag
    extra = 0
    max_num = 3

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = super().get_max_num(request, obj, **kwargs)
        return min(max_num, 3) if max_num is not None else 3


@admin.register(Accommodation)
class AccommodationAdmin(SummernoteModelAdmin):
    form = AccommodationForm
    fieldsets = (
        ('분류', {'fields': ('category', 'status', )}),
        ('숙소 정보', {'fields': ('name_kr', 'poster', 'name_en', 'address', 'phone', 'reservation_link')}),
        ('숙소 상세 페이지 에디터', {'fields': ('content', )})
    )
    readonly_fields = ('created_at', 'updated_at', )
    list_display = ['abstract_name', 'status', 'category', 'reservation_link', 'created_at', 'updated_at']
    list_filter = ['status', 'category', 'created_at', 'updated_at']
    search_fields = ['name_kr', 'name_en']
    summernote_fields = ['content',]
    inlines = [AccommodationTagInline]

    def abstract_name(self, obj):
        return f"{obj.name_kr}({obj.name_en})"

    abstract_name.short_description = '숙소 명'
