from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.urls import reverse
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework_simplejwt.tokens import RefreshToken, Token
from rest_framework_swagger import renderers
from api.permissions import IsAuthenticatedOrReadOnly
from api.serializers import UserSerializer
from core.models import User
from api.tasks import send_email_task


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    # renderer_classes = [
    #     renderers.OpenAPIRenderer,
    #     renderers.SwaggerUIRenderer
    # ]

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        # for i in range(len(serializer.data)):
        #     if serializer.data[i]['role'] == 1:
        #         serializer.data[i]['role'] = 'Ordinary User'
        #     elif serializer.data[i]['role'] == 2:
        #         serializer.data[i]['role'] = 'Company'
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            user = User.objects.get(email=serializer_data['email'])
            uid = force_str(urlsafe_base64_encode(force_bytes(user.id)))

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

    def update(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, pk=None):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
