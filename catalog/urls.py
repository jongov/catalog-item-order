from django.contrib import admin
from django.urls import path
from . import views
from .views import VideoListAPIView, SeasonListAPIView, TVShowListAPIView

urlpatterns = [
    path("videos/", VideoListAPIView.as_view(), name='video-list'),
    path("seasons/", SeasonListAPIView.as_view(), name='season-list'),
    path("tvshows/", TVShowListAPIView.as_view(), name='tvshow-list'),
]