from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from api.serializers import RequestSerializer
from core.models import RequestModel
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response


class RequestViewSet(viewsets.ModelViewSet):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = RequestModel.objects.all()
        serializer = RequestSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = RequestModel.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = RequestSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        req = get_object_or_404(RequestModel, pk=pk)
        serializer = RequestSerializer(instance=req, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        user = get_object_or_404(RequestModel, pk=pk)
        serializer = RequestSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
