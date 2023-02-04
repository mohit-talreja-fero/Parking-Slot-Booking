from django.contrib import admin

from .models import Account, NormalUser, CareTakerUser


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'account_type', 'phone_number', 'user')
    list_filter = ('user',)


@admin.register(NormalUser)
class NormalUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'has_premium', 'premium_expiry')
    list_filter = ('user', 'has_premium', 'premium_expiry')


@admin.register(CareTakerUser)
class CareTakerUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_filter = ('user',)
