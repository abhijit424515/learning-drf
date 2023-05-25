from django.urls import path, include
from watchlist_app.views import movie_list, nth_movie_details

urlpatterns = [
    path('list/',movie_list, name='movie_list'),
    path('nth-movie/<int:pk>',nth_movie_details, name='nth_movie_details')
]
