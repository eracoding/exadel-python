from rest_framework import viewsets
from api.serializers import ServiceSerializer
from core.models import Service


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
