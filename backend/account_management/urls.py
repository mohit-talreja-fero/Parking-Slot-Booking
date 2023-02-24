from django.urls import path
from account_management.views import LoginView, LogoutView, RegisterUserView, \
    UserProfileView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<int:pk>/", UserProfileView.as_view(), name="account"),
    path("create/", RegisterUserView.as_view(), name="account-create"),
]
