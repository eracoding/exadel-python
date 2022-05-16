from rest_framework import viewsets
from api.serializers import ReviewSerializer
from core.models import Review


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
