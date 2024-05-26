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
        read_only_fields = [
            "account_id",
            "app_secret_token",
        ]

    def validate(self, attrs):
        for field in self.Meta.read_only_fields:
            if field in self.initial_data:
                raise serializers.ValidationError({field: "This field is read-only and cannot be modified."})
        return attrs
