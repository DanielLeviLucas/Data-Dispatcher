from django.urls import path

from apps.api.v1.accounts.views import AccountListCreate, AccountUpdateView

app_name = "accounts"

urlpatterns = [
    path("", AccountListCreate.as_view(), name="list_create"),
    path("<uuid:account_id>/update/", AccountUpdateView.as_view(), name="update"),
]
