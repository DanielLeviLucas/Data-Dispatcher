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

    def validate(self, attrs):
        for field in self.Meta.read_only_fields:
            if field in self.initial_data:
                raise serializers.ValidationError({field: "This field is read-only and cannot be modified."})
        return attrs


class DestinationUpdateSerializer(DestinationSerializer):
    account_id = serializers.UUIDField(source="account.account_id", read_only=True)

    class Meta(DestinationSerializer.Meta):
        model = Destination
        fields = DestinationSerializer.Meta.fields
        read_only_fields = DestinationSerializer.Meta.read_only_fields + ["account_id"]
