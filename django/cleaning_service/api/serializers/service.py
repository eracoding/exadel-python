from rest_framework import serializers
from core.models import Service, User
from api.serializers.user import UserSerializer
from core.utility import decode_uid


class AttrCMPField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        queryset = User.objects.filter(role=1)
        return queryset


class ServiceSerializer(serializers.ModelSerializer):
    company_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role=2, is_active=True))

    class Meta:
        model = Service
        fields = ('id', 'name', 'cost', 'company_id')

    # def create(self, validated_data):
    #     company = User.objects.get(company_id=decode_uid(validated_data['company_id']))
    #     obj = self.Meta.model(**validated_data)
    #     obj.company_id = company
    #     obj.save()
    #     print("ITS RUNNING")
    #     return obj

    # def get_companies(self):
    #     companies = User.objects.all().filter(role=2)
    #     serializer = UserSerializer(instance=companies, many=True, context=self.context)
    #
    #     return companies
