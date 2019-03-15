from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'moviedb'
urlpatterns = [
    # movies
    path('movies/', views.MovieListView.as_view(), name='movie'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(),
         name='movie_detail'),
    path('movies/create/', views.MovieCreateView.as_view(),
         name='create_movie'),
    path('movies/update/<int:pk>/', views.MovieUpdateView.as_view(),
         name='update_movie'),
    path('movies/delete/<int:pk>/', views.MovieDeleteView.as_view(),
         name='delete_movie'),

    path('movies/comments/<int:pk>/update/',
         views.CommentMovieUpdateView.as_view(), name='update_commentmovie'),
    path('movies/comments/<int:pk>/delete/',
         views.CommentMovieDeleteView.as_view(), name='delete_commentmovie'),

    # actors
    path('actors/', views.ActorListView.as_view(), name='actor'),
    path('actors/<int:pk>/', views.ActorDetailView.as_view(),
         name='actor_detail'),
    path('actors/create/', views.ActorCreateView.as_view(),
         name='create_actor'),
    path('actors/update/<int:pk>/', views.ActorUpdateView.as_view(),
         name='update_actor'),
    path('actors/delete/<int:pk>/', views.ActorDeleteView.as_view(),
         name='delete_actor'),

    path('actors/comments/<int:pk>/update/',
         views.CommentActorUpdateView.as_view(), name='update_commentactor'),
    path('actors/comments/<int:pk>/delete/',
         views.CommentActorDeleteView.as_view(), name='delete_commentactor'),

    # awards
    path('awards/', views.AwardListView.as_view(), name='award'),
    path('awards/<int:pk>/', views.AwardDetailView.as_view(),
         name='award_detail'),
    path('awards/create/', views.AwardCreateView.as_view(),
         name='create_award'),
    path('awards/update/<int:pk>/', views.AwardUpdateView.as_view(),
         name='update_award'),
    path('awards/delete/<int:pk>/', views.AwardDeleteView.as_view(),
         name='delete_award'),

    path('awards/comments/<int:pk>/update/',
         views.CommentAwardUpdateView.as_view(), name='update_commentaward'),
    path('awards/comments/<int:pk>/delete/',
         views.CommentAwardDeleteView.as_view(), name='delete_commentaward'),
]
