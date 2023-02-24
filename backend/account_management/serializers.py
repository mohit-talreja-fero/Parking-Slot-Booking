from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils import timezone
from rest_framework.authtoken.serializers import AuthTokenSerializer

from account_management import utils, models
from lib import constants


class NormalUserProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    username = serializers.CharField(source="user.username")
    password = serializers.CharField(source="user.password", write_only=True)

    class Meta:
        model = models.NormalUser
        fields = (
            "first_name", "last_name", "username", "has_premium", "password",
        )

    def validate_username(self, username):
        if User.objects.filter(username__iexact=username).exists():
            raise serializers.ValidationError(f"User with username {username} is already registered."
                                              f"Please choose different username")
        return username

    def validate(self, attrs):  # Move to field validation
        premium_expiry = attrs.get("premium_expiry", None)
        if premium_expiry and premium_expiry <= timezone.now():
            raise serializers.ValidationError({"premium_expiry": "Premium Expiry cannot be in Past"})

        attrs["has_premium"] = True
        return super(NormalUserProfileSerializer, self).validate(attrs=attrs)

    def create(self, validated_data):
        user = validated_data.pop("user")
        password = user.pop("password")
        user: User = User.objects.create_user(**user, password=password)
        # user.set_password(raw_password=password)
        validated_data["user"] = user
        return super(NormalUserProfileSerializer, self).create(validated_data=validated_data)


class AccountDetailSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    username = serializers.CharField(source="user.username")
    account_type = serializers.CharField(source="get_account_type_display")

    class Meta:
        model = models.Account
        fields = (
            "first_name", "last_name", "username",
        )


# class LoginSerializer(AuthTokenSerializer):
