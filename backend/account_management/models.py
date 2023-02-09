from django.contrib.auth.models import User
from django.db import models
from lib import constants, choices


class Account(models.Model):
    account_type = models.CharField(
        max_length=25, choices=choices.ACCOUNT_TYPE_CHOICES, default=constants.AccountType.NORMAL)

    phone_number = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class NormalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_premium = models.BooleanField(default=False)
    premium_expiry = models.DateTimeField(null=True, blank=True)


class CareTakerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Membership(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    premium_type = models.CharField(max_length=16, default="PREM")

    def __str__(self):
        return f"MEM-{self.account.user.username} - {self.start_time}"
