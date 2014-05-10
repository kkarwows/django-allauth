from allauth.socialaccount import models


def socialaccount(request):
    ctx = {'providers': models.get_enabled_providers()}
    return dict(socialaccount=ctx)
