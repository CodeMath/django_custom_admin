from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from cms_admin.models import *
from django.utils.safestring import mark_safe
from django.contrib.auth.models import Group

from cms_admin.forms import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

admin.site.unregister(Group)
admin.site.unregister(User)


class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    list_display = ['username', 'first_name_custom', 'last_name_custom', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('계정 정보', {'fields': ('first_name', 'last_name', 'email')}),
        ('권한', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('회원가입일 및 마지막 로그인', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ()

    def first_name_custom(self, obj):
        return obj.first_name

    first_name_custom.short_description = _("직책")

    def last_name_custom(self, obj):
        return obj.last_name

    last_name_custom.short_description = _("이름")

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == "first_name":
            field.label = _("직책")
        elif db_field.name == "last_name":
            field.label = _("이름")
        return field


admin.site.register(User, CustomUserAdmin)


class NoticeAttachmentInline(admin.TabularInline):
    model = NoticeAttachment
    extra = 0


@admin.register(Notice)
class NoticeAdmin(SummernoteModelAdmin):
    form = NoticeForm
    fieldsets = (
        ('공지사항', {'fields': ('title', )}),
        ('정보', {'fields': ('view_count', 'created_at', 'updated_at')}),
        ('내용', {'fields': ('content',)}),
    )
    inlines = [NoticeAttachmentInline]
    readonly_fields = ('created_at', 'updated_at')  # 읽기 전용 필드 설정 추가
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    summernote_fields = ('content', )


class QuestionAttachmentInline(admin.TabularInline):
    model = QuestionAttachment
    extra = 0


@admin.register(Question)
class QuestionAdmin(SummernoteModelAdmin):
    form = QuestionForm
    fieldsets = (
        ('FAQ', {'fields': ('title',)}),
        ('정보', {'fields': ('view_count', 'created_at', 'updated_at')}),
        ('내용', {'fields': ('content',)}),
    )
    inlines = [QuestionAttachmentInline]
    readonly_fields = ('created_at', 'updated_at')  # 읽기 전용 필드 설정 추가
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    summernote_fields = ('content', )


class FacilityTagInline(admin.TabularInline):
    model = FacilityTag
    extra = 0
    max_num = 3

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = super().get_max_num(request, obj, **kwargs)
        return min(max_num, 3) if max_num is not None else 3


@admin.register(Facility)
class FacilityAdmin(SummernoteModelAdmin):
    form = FacilityAdminForm
    list_display = ('title', 'get_category_display', 'open_time', 'close_time')
    fieldsets = (
        ('시설 정보', {'fields': ('title', 'category', 'address',)}),
        ('정보 입력', {'fields': ('poster', 'content')}),
        ('영업 시간', {'fields': ('open_time', 'close_time')}),
    )
    search_fields = ('title', 'address')
    inlines = [FacilityTagInline]

    def get_category_display(self, obj):
        return ', '.join([dict(Facility.CATEGORY_TYPES).get(cat, cat) for cat in obj.category])

    get_category_display.short_description = '카테고리'
