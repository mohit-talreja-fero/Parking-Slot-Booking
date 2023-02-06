from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


def generate_user_token(user: User):
    token, created = Token.objects.get_or_create(user=user)
    return token.key
