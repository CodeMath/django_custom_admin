from django.utils.html import format_html
from django.contrib import admin
from cms_bbs.forms import *


class GalleryAttachmentInline(admin.TabularInline):
    model = GalleryAttachment
    extra = 0
    fields = ('url', 'ordering', 'image_preview')
    ordering = ('ordering',)
    readonly_fields = ('image_preview',)

    def image_preview(self, instance):
        if instance.url:
            return format_html('<img src="{}" width="100" height="100">', instance.url.url)
        return "No Image"

    image_preview.short_description = '미리보기'

    class Media:
        js = ('admin/js/image_previews.js',)


@admin.register(GallerySession)
class GallerySessionAdmin(admin.ModelAdmin):
    form = GallerySessionForm
    fieldsets = (
        (None, {'fields': ('year', 'session')}),
    )
    readonly_fields = ('session',)
    list_display = ('year', 'session')
    list_filter = ('year',)
    ordering = ('-year',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    form = GalleryForm
    fieldsets = (
        ('카테고리', {'fields': ('status', 'category', 'session')}),
        ('갤러리', {'fields': ('poster', 'description')})
    )
    inlines = [GalleryAttachmentInline]
    list_display = ('session', 'category', 'image_preview', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'category', 'session')
    ordering = ('-session__year', )
    date_hierarchy = 'created_at'


    def image_preview(self, obj):
        total_attachments = obj.galleryattachment_set.count()
        attachments = obj.galleryattachment_set.all()[:5]
        images_html = []
        for attachment in attachments:
            images_html.append(
                format_html('<img src="{}" width="50" height="50" style="margin-right: 15px; border:1px solid #eee;"/>', attachment.url.url))
        more_count = total_attachments - 5
        if more_count > 0:
            images_html.append(format_html('<span style="line-height: 100px;">+{}개 더 있음</span>', more_count))
        return format_html(''.join(images_html)) if images_html else "No Image"

    image_preview.short_description = '이미지 미리보기'

