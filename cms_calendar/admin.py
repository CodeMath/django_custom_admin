from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from cms_calendar.forms import *


class EventAttachmentAdmin(admin.TabularInline):
    model = EventAttachment


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    form = Event
    fieldsets = (
        ('설정', {'fields': ('status', 'start', 'end')}),
        ('이벤트 내용', {'fields': ('title', 'description', 'poster', )}),
        ('내용', {'fields': ('content', )}),
    )
    inlines = [EventAttachmentAdmin]
    list_display = ('title', 'status', 'start', 'end', 'description')
    list_filter = ('status', )
    search_fields = ('title', 'description', 'content')


class MarketAttachmentAdmin(admin.TabularInline):
    model = MarketAttachment


@admin.register(Market)
class MarketAdmin(SummernoteModelAdmin):
    form = MarketForm
    fieldsets = (
        ('마켓 정보', {'fields': ('status', 'title', 'description', 'poster')}),
        ('오픈 시간', {'fields': ('start', 'end', 'start_time', 'end_time')}),
        ('내용', {'fields': ('content', )}),
    )
    inlines = [MarketAttachmentAdmin]
    list_display = ('title', 'status', 'start', 'end', )
    list_filter = ('status', )
    search_fields = ('title', 'description')