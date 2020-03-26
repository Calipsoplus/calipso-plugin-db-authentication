from django.conf import settings
from django.urls import path

from cp_authentication.views.login import login_user, logout_user

if settings.EXTERNAL_LOGIN_ACTIVE:
    urlpatterns = [
        path('login/', login_user, name='login_url'),
        path('logout/', logout_user, name='logout_url'),
    ]
else:
    urlpatterns = []
