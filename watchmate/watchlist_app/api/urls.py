from django.urls import path, include
# For functional api view
# from watchlist_app.views import movie_list, movie_detail

# For class api view
from watchlist_app.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
    path('movies/', MovieListAV.as_view(), name='movie_list'),
    path('movie/<int:pk>', MovieDetailAV.as_view(), name='movie_detail')
]
