from django.contrib.auth.models import User
from rest_framework import serializers

from account_management import utils, models
from lib import constants


class NormalUserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    password = serializers.CharField(required=True, allow_null=False, allow_blank=False, write_only=True)

    def validate(self, attrs):
        username = attrs.pop("username")
        password = attrs.pop("password")

        try:
            user = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid Credentials")

        if not user.check_password(raw_password=password):
            raise serializers.ValidationError("Invalid Credentials")

        token = utils.generate_user_token(user=user)
        attrs["token"] = token
        return super(NormalUserLoginSerializer, self).validate(attrs=attrs)


class NormalUserProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    username = serializers.CharField(source="user.username")
    premium_expiry = serializers.DateTimeField(
        format=constants.GeneralConstants.DATE_TIME_FORMAT)

    class Meta:
        model = models.NormalUser
        fields = (
            "first_name", "last_name", "username", "has_premium", "premium_expiry",
        )
