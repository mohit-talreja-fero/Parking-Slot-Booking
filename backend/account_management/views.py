from rest_framework import views, status, generics, permissions, authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from account_management import serializers, utils, models


class LoginView(views.APIView):
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = serializers.NormalUserLoginSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "message": "Logged In Successfully!", **serializer.validated_data},
            status=status.HTTP_200_OK)


class NormalUserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.NormalUserProfileSerializer
    queryset = models.NormalUser


class ProfileDetailView(views.APIView):
    permission_classes = [permissions.AllowAny,]
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({"wow": "wow", }, status=200)
