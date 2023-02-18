from django.urls import path
from account_management.views import LoginView, NormalUserProfileView, ProfileDetailView, LogoutView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<int:pk>/", NormalUserProfileView.as_view(), name="account"),
    path("", ProfileDetailView.as_view(), name="account"),
]
