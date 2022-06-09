from rest_framework import serializers
from core.models import Service, User
from api.serializers.user import UserSerializer


class AttrCMPField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        queryset = User.objects.filter(role=1)
        return queryset


class ServiceSerializer(serializers.ModelSerializer):
    company_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role=2))

    class Meta:
        model = Service
        fields = ('id', 'name', 'cost', 'company_id')

    # def get_companies(self):
    #     companies = User.objects.all().filter(role=2)
    #     serializer = UserSerializer(instance=companies, many=True, context=self.context)
    #
    #     return companies
