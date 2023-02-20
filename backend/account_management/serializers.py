from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils import timezone

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
        attrs["user_type"] = constants.AccountType.NORMAL
        return super(NormalUserLoginSerializer, self).validate(attrs=attrs)


class NormalUserProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    username = serializers.CharField(source="user.username")
    premium_expiry = serializers.DateTimeField(
        format=constants.GeneralConstants.DATE_TIME_FORMAT, allow_null=True)

    class Meta:
        model = models.NormalUser
        fields = (
            "first_name", "last_name", "username", "has_premium", "premium_expiry",
        )

    def validate_username(self, username):
        if User.objects.filter(username__iexact=username).exists():
            raise serializers.ValidationError(f"User with username {username} is already registered."
                                              f"Please choose different username")
        return username

    def validate(self, attrs):
        premium_expiry = attrs.get("premium_expiry", None)
        if premium_expiry and premium_expiry <= timezone.now():
            raise serializers.ValidationError({"premium_expiry": "Premium Expiry cannot be in Past"})

        attrs["has_premium"] = True
        return super(NormalUserProfileSerializer, self).validate(attrs=attrs)

    def create(self, validated_data):
        user = validated_data.pop("user")
        user = User.objects.create(**user)
        validated_data["user"] = user
        return super(NormalUserProfileSerializer, self).create(validated_data=validated_data)


class AccountLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    password = serializers.CharField(required=True, allow_null=False, allow_blank=False, write_only=True)

    def validate(self, attrs):
        username = attrs.pop("username")
        password = attrs.pop("password")

        try:
            account = models.Account.objects.get(user__username=username)
            user = account.user

        except models.Account.DoesNotExist:
            raise serializers.ValidationError("Invalid Credentials")

        if not user.check_password(raw_password=password):
            raise serializers.ValidationError("Invalid Credentials")

        token = utils.generate_user_token(user=user)
        attrs["token"] = token
        attrs["user_type"] = constants.AccountType.NORMAL
        return super(AccountLoginSerializer, self).validate(attrs=attrs)


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
