from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    print(movies.values())

    return JsonResponse({'movies': list(movies.values())})

def nth_movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)  # pk = primary key

    return JsonResponse({'movie': {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active
    }})