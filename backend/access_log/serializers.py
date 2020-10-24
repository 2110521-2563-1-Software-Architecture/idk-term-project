from rest_framework import serializers
from access_log.models import AccessLog


class AccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessLog
        fields = "__all__"
