from allauth.socialaccount.models import SocialApp


def socialaccount(request):
    ctx = {'providers': SocialApp.objects.values_list('provider', flat=True)}
    return dict(socialaccount=ctx)
