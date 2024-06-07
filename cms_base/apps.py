from django.apps import AppConfig


class CmsBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cms_base'
    verbose_name = "CMS 설정"
