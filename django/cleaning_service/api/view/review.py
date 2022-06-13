from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from core.utility import encode_uid, decode_uid
from core.models import Review
from api.serializers import ReviewSerializer
from api.permissions import ReviewPermission


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewPermission]

    @action(detail=False, methods=['get'])
    def list(self, request):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        for i in range(len(serializer.data)):
            serializer.data[i]['id'] = encode_uid(serializer.data[i]['id'])
            serializer.data[i]['user_id'] = encode_uid(serializer.data[i]['user_id'])
            serializer.data[i]['service_id'] = encode_uid(serializer.data[i]['service_id'])
            serializer.data[i]['request_id'] = encode_uid(serializer.data[i]['request_id'])
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def retrieve(self, request, pk=None):
        queryset = Review.objects.all()
        review = get_object_or_404(queryset, pk=decode_uid(pk))
        if review.user_id.id == request.user.id or request.user.is_admin:
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=False, methods=['post'])
    def create(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            if str(request.user.id) == request.data['user_id'] or request.user.is_admin:
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(status.HTTP_405_METHOD_NOT_ALLOWED)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['post', 'put'])
    def update(self, request, pk=None):
        review = get_object_or_404(Review, pk=decode_uid(pk))
        if review.user_id.id == request.user.id or request.user.is_admin:
            serializer = ReviewSerializer(instance=review, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        review = get_object_or_404(Review, pk=decode_uid(pk))
        if request.user.id == review.user_id.id or request.user.is_admin:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)
