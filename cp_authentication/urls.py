from django.conf import settings
from django.conf.urls import url

from cp_authentication.views.login import login_user, logout_user

if settings.EXTERNAL_LOGIN_ACTIVE:
    urlpatterns = [
        url(r'^login$', login_user, name='login_url'),
        url(r'^logout$', logout_user, name='logout_url'),
    ]
else:
    urlpatterns = []
