from django.urls import path, include

from watchlist_app.views import movie_list, movie_detail

urlpatterns = [
    path('movies/', movie_list, name='movie_list'),
    path('movie/<int:pk>', movie_detail, name='movie_detail')
]
