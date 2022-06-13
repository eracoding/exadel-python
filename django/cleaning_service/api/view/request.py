from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from core.utility import encode_uid, decode_uid
from core.models import RequestModel, User
from api.serializers import RequestSerializer
from api.permissions import RequestPermission


class RequestViewSet(viewsets.ModelViewSet):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [RequestPermission]

    @action(detail=False, methods=['get'])
    def list(self, request):
        if request.user.is_admin:
            queryset = RequestModel.objects.all()
        else:
            queryset = RequestModel.objects.filter(user_id=request.user.id)
        serializer = RequestSerializer(queryset, many=True)
        for i in range(len(serializer.data)):
            serializer.data[i]['id'] = encode_uid(serializer.data[i]['id'])
            serializer.data[i]['user_id'] = encode_uid(serializer.data[i]['user_id'])
            serializer.data[i]['service_id'] = encode_uid(serializer.data[i]['service_id'])
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def retrieve(self, request, pk=None):
        queryset = RequestModel.objects.all()
        req = get_object_or_404(queryset, pk=decode_uid(pk))
        if request.user.id == req.user_id.id or request.user.is_admin:
            serializer = RequestSerializer(req)
            return Response(serializer.data)
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=False, methods=['post'])
    def create(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            if str(request.user.id) == request.data['user_id'] or request.user.is_admin:
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(status.HTTP_405_METHOD_NOT_ALLOWED)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['post', 'put'])
    def update(self, request, pk=None):
        req = get_object_or_404(RequestModel, pk=decode_uid(pk))
        if request.user.id == req.user_id.id or request.user.is_admin:
            serializer = RequestSerializer(instance=req, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        req = get_object_or_404(RequestModel, pk=decode_uid(pk))
        if request.user.id == req.user_id.id or request.user.is_admin:
            req.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)
