from rest_framework import serializers
from core.models import RequestModel, User


class RequestSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role=1, is_active=True))
    # service_id = serializers.SerializerMethodField()
    # requestStatus_id = serializers.SerializerMethodField()

    class Meta:
        model = RequestModel
        fields = ('id', 'user_id', 'service_id', 'requestStatus_id', 'area_total', 'address', 'created_at', 'cost_total')
        extra_kwargs = {
            'cost_total': {'read_only': True}
        }

    # def get_user_id(self, obj):
    #     return obj.user_id.fullname
    #
    # def get_service_id(self, obj):
    #     return obj.service_id.name
    #
    # def get_requestStatus_id(self, obj):
    #     return str(obj.requestStatus_id)
