from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('parking/', include("space.urls")),
    path('account/', include("account_management.urls")),
]
