from rest_framework import serializers
from rest_framework.serializers import Serializer


class DeviceSerializer(Serializer):
    id = serializers.CharField(allow_null=False)
    deviceModel = serializers.CharField(allow_null=False)
    name = serializers.CharField(allow_null=False)
    note = serializers.CharField(allow_null=False)
    serial = serializers.CharField(allow_null=False)

    def validate_id(self, value):
        if value.startswith("/devices/id") and value[11:].isdigit():
            return value
        else:
            raise serializers.ValidationError(
                "enter id in this format: /devices/id<pk>"
            )
