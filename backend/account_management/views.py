from rest_framework import views, status, generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from account_management import serializers, utils, models


class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        data = {"token": token.key}
        return Response(data=data, status=status.HTTP_200_OK)


class LogoutView(views.APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        user.auth_token.delete()
        return Response(status=status.HTTP_205_RESET_CONTENT)


class NormalUserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.NormalUserProfileSerializer
    queryset = models.NormalUser


class RegisterNormalUserProfileView(generics.CreateAPIView):
    serializer_class = serializers.NormalUserProfileSerializer
    queryset = models.NormalUser
    authentication_classes = []
    permission_classes = (permissions.AllowAny,)
