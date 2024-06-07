from django.apps import AppConfig


class CmsCalendarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cms_calendar'
    verbose_name = "이벤트 일정 관리"