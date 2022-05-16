from rest_framework import serializers
from core.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()
    service_id = serializers.SerializerMethodField()
    request_id = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('user_id', 'service_id', 'request_id', 'rating', 'feedback', 'created_at')

    def get_user_id(self, obj):
        return str(obj.user_id.fullname)

    def get_service_id(self, obj):
        return str(obj.service_id.name)

    def get_request_id(self, obj):
        return str(obj.request_id)
