from rest_framework import generics
from api.serializers import RequestSerializer
from core.models import Request


class RequestListView(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestCreateView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestDeleteView(generics.DestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

