from rest_framework import serializers
from core.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    company_id = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ('name', 'cost', 'company_id')

    def get_company_id(self, obj):
        return obj.company_id.fullname
