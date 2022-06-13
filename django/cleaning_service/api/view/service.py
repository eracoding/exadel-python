from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from api.serializers import ServiceSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from core.utility import encode_uid, decode_uid
from core.models import Service
from api.permissions import ServicePermission


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    # permission_classes = [ServicePermission]
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'])
    def list(self, request):
        queryset = Service.objects.all()
        serializer = ServiceSerializer(queryset, many=True)
        for i in range(len(serializer.data)):
            serializer.data[i]['id'] = encode_uid(serializer.data[i]['id'])
            serializer.data[i]['company_id'] = encode_uid(serializer.data[i]['company_id'])
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def retrieve(self, request, pk=None):
        queryset = Service.objects.all()
        service = get_object_or_404(queryset, pk=decode_uid(pk))
        if request.user.id == service.company_id.id or request.user.is_admin:
            serializer = ServiceSerializer(service)
            return Response(serializer.data)
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=False, methods=['post'])
    def create(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            if str(request.user.id) == request.data['company_id'] or request.user.is_admin:
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(status.HTTP_405_METHOD_NOT_ALLOWED)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['post', 'put'])
    def update(self, request, pk=None):
        service = get_object_or_404(Service, pk=decode_uid(pk))
        if request.user.id == service.company_id.id or request.user.is_admin:
            serializer = ServiceSerializer(instance=service, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        service = get_object_or_404(Service, pk=decode_uid(pk))
        if request.user.id == service.company_id.id or request.user.is_admin:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)
