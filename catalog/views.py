from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from .models import Video, Season, TVShow
from .serializers import VideoSerializer, SeasonSerializer, TVShowSerializer

class VideoListAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_queryset(self):
        queryset = Video.objects.all()
        order_param = self.request.query_params.get('order', None)

        if order_param:
            # You can customize the logic here based on the order_param value
            if order_param == 'title':
                queryset = queryset.order_by('title')
            elif order_param == 'creation_datetime':
                queryset = queryset.order_by('creation_datetime')

        return queryset    
                
class SeasonListAPIView(generics.ListAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer    

class TVShowListAPIView(generics.ListAPIView):
    queryset = TVShow.objects.all()
    serializer_class = TVShowSerializer

    def get_queryset(self):
        queryset = TVShow.objects.all()
        order_param = self.request.query_params.get('order', None)

        if order_param:
            # You can customize the logic here based on the order_param value
            if order_param == 'title':
                queryset = queryset.order_by('title')
            elif order_param == 'last_episode':
                queryset = queryset.order_by('last_episode_creation_datetime')

        return queryset