from rest_framework import serializers
from apps.accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "account_id",
            "email_id",
            "app_secret_token",
            "account_name",
            "website",
        ]
