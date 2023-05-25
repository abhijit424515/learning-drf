from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movie_list(request):
    match request.method:
        case "GET":
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)
        case "POST":
            serializer = MovieSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def nth_movie_details(request, pk):
    match request.method:
        case "GET":
            try:
                movie = Movie.objects.get(pk=pk)
                serializer = MovieSerializer(movie)
                return Response(serializer.data)
            except Movie.DoesNotExist:
                return Response(
                    {"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
                )

        case "PUT":
            try:
                movie = Movie.objects.get(pk=pk)
                serializer = MovieSerializer(movie, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(
                        serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )
            except Movie.DoesNotExist:
                return Response(
                    {"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
                )

        case "DELETE":
            try:
                movie = Movie.objects.get(pk=pk)
                movie.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Movie.DoesNotExist:
                return Response(
                    {"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
                )
