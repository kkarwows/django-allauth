try:
    from django.apps import AppConfig
except ImportError:
    class AppConfig:
        pass

from django.utils.translation import ugettext_lazy as _


class AllAuthConfig(AppConfig):
    name = 'allauth.socialaccount'
    verbose_name = _('Socialaccount')