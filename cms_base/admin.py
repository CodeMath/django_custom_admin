from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from cms_base.models import *

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


@admin.register(Attachment)
class AdminSite(admin.ModelAdmin):
    list_display = ['id', 'url']
    search_fields = ['url']
