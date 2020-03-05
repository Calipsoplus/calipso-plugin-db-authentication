import logging

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from cp_authentication.auth.backends import ExternalDatabaseAuthenticationBackend
from cp_authentication.utils import JSONResponse

logger = logging.getLogger(__name__)
external_auth = ExternalDatabaseAuthenticationBackend()

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        logger.debug('POST login view')
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            remote_user = external_auth.authenticate(request, username=username, password=password)
        except Exception as e:
            logger.debug('Authenticate database error:%s' % e)
            return JSONResponse({'error': 'HTTP_400_BAD_REQUEST'}, status=status.HTTP_400_BAD_REQUEST)

        if remote_user is None:
            logger.debug('User not found or incorrect password')
            return JSONResponse({'error': 'HTTP_401_UNAUTHORIZED'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            logger.debug('Get or Create for username:%s in local db' % username)

            user, created = User.objects.using('default').get_or_create(username=username)
            if created:
                user.set_password(password)
                user.save()

            data = {'username': username}
            return JSONResponse(data, status=status.HTTP_200_OK)

    return JSONResponse({'error': 'METHOD NOT ALLOWED'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def logout_user(request):
    logout(request)
    return JSONResponse({'message': 'logout_user done'}, status=status.HTTP_200_OK)


def test_user(request):
    return render(request, 'login.html')
