from django.urls import path

from apps.api.v1.accounts.views import AccountListCreate

app_name = "accounts"

urlpatterns = [
    path("", AccountListCreate.as_view(), name="list_create"),
]
