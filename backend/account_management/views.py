from rest_framework import views, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from account_management import serializers, utils


class LoginView(views.APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = serializers.NormalUserLoginSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "message": "Logged In Successfully!", **serializer.validated_data},
            status=status.HTTP_200_OK)
