from rest_framework import viewsets
from api.serializers import RequestSerializer
from core.models import Request


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
