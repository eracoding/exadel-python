from django.utils.text import slugify
from rest_framework import serializers
from core.models import User


class UserSerializer(serializers.ModelSerializer):
    # role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'fullname', 'phone', 'email', 'role', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # def get_role(self, obj):
    #     return str(obj.role)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        obj = self.Meta.model(**validated_data)
        if password is not None:
            obj.set_password(password)
        obj.save()
        return obj


