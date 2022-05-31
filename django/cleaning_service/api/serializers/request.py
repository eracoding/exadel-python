from rest_framework import serializers
from core.models import RequestModel


class RequestSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()
    company_id = serializers.SerializerMethodField()
    requestStatus_id = serializers.SerializerMethodField()

    class Meta:
        model = RequestModel
        fields = ('user_id', 'company_id', 'requestStatus_id', 'cost_total', 'address', 'created_at')

    def get_user_id(self, obj):
        return obj.user_id.fullname

    def get_company_id(self, obj):
        return obj.company_id.fullname

    def get_requestStatus_id(self, obj):
        return str(obj.requestStatus_id)
