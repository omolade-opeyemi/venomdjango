import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth.models import User



class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        print('auth', auth_data)
        if not auth_data:
            return None
        token = auth_data.decode('utf-8')
        print('decoded', token)
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY,algorithms=['HS256', 'RS256'])
            user=User.objects.get(username=payload['username'])
            return (user, token)
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('Your token is invalid, login')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed('Your token is expired, login')
            