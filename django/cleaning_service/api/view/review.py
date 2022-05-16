from api.serializers import ReviewSerializer
from core.models import Review
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def list(self, request):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Review.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ReviewSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk=None):
        user = get_object_or_404(Review, pk=pk)
        serializer = ReviewSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
