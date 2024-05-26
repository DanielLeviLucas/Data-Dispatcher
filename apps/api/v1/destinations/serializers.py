from rest_framework import serializers
from apps.destinations.models import Destination


class DestinationSerializer(serializers.ModelSerializer):
    account_id = serializers.UUIDField(source="account.account_id")

    class Meta:
        model = Destination
        fields = [
            "id",
            "account_id",
            "url",
            "http_method",
            "headers",
        ]
        read_only_fields = [
            "id",
        ]
