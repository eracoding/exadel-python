from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.db.models import Q

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework_swagger import renderers

from api.permissions import UserPermission
from api.serializers import UserSerializer
from core.models import User
from api.tasks import send_email_task
from core.utility import encode_uid, decode_uid


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)
    # renderer_classes = [
    #     renderers.OpenAPIRenderer,
    #     renderers.SwaggerUIRenderer
    # ]

    @action(detail=False, methods=['get'])
    def list(self, request):
        if request.user.is_authenticated:
            if request.user.is_admin:
                queryset = User.objects.all()
            else:
                queryset = User.objects.filter(Q(id=request.user.id) | Q(role=2))
        else:
            queryset = User.objects.filter(Q(role=2))
        serializer = self.get_serializer(queryset, many=True)
        for i in range(len(serializer.data)):
            serializer.data[i]['id'] = encode_uid(serializer.data[i]['id'])
            if serializer.data[i]['role'] == 1:
                serializer.data[i]['role'] = 'Ordinary User'
            elif serializer.data[i]['role'] == 2:
                serializer.data[i]['role'] = 'Company'
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=decode_uid(pk))
        if request.user == user or request.user.is_admin:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=False, methods=['post'])
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            user = User.objects.get(email=serializer_data['email'])
            uid = encode_uid(user.id)

            token = default_token_generator.make_token(user)

            protocol = 'https://' if request.is_secure() else 'http://'
            cur_site = get_current_site(request).domain
            absurl = f'{protocol}{cur_site}/api/activate/{uid}/{str(token)}'

            email_body = f'Hello, {user.fullname}\nUse the following link to verify your account: \n{absurl}'
            data = {'send_to': user.email, 'email_body': email_body, 'email_subject': 'Verify email'}

            send_email_task.delay(data)
            messages.success(request, 'Successfuly sent activation email')

            return Response(serializer_data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['put', 'post'])
    def update(self, request, pk=None):
        user = get_object_or_404(User, pk=decode_uid(pk))
        if request.user == user or request.user.is_admin:
            serializer = self.get_serializer(instance=user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        user = get_object_or_404(User, pk=decode_uid(pk))
        if request.user == user or request.user.is_admin:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)
