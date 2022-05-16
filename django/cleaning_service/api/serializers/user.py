from rest_framework import serializers
from core.models import User


class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('fullname', 'phone', 'email', 'role')

    def get_role(self, obj):
        return str(obj.role)
