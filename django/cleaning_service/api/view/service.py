from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.serializers import ServiceSerializer
from core.models import Service
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response


class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def list(self, request):
        queryset = Service.objects.all()
        serializer = ServiceSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Service.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ServiceSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk=None):
        user = get_object_or_404(Service, pk=pk)
        serializer = ServiceSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
