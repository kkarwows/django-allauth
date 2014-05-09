from . import providers
from allauth.socialaccount.models import SocialApp


def socialaccount(request):
    all_providers = providers.registry.get_list()
    configured = SocialApp.objects.values_list('provider', flat=True)
    ctx = {'providers':  filter(lambda x: x.id in configured, all_providers)}
    return dict(socialaccount=ctx)
