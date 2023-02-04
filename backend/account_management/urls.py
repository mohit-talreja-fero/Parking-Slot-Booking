from django.urls import path
from account_management.views import LoginView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
]
