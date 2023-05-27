from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import (
    WatchListSerializer,
    StreamPlatformSerializer,
    ReviewSerializer,
)


class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Review.objects.filter(watchlist=pk)


class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        show = WatchList.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=show, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this show")

        serializer.save(watchlist=show, review_user=review_user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


# class StreamPlatformVS(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


class StreamPlatformListAV(APIView):
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(
            platforms, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(movie)
            return Response(serializer.data)
        except StreamPlatform.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except StreamPlatform.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except StreamPlatform.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)


class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(movie)
            return Response(serializer.data)
        except WatchList.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except WatchList.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except WatchList.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
