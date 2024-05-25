from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
app_name = "api_v1"

urlpatterns = [
    path("account/", include("apps.api.v1.accounts.urls", namespace="accounts")),
    path("auth_token/", obtain_auth_token, name="auth_token"),
]
