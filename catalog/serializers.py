from rest_framework import serializers
from .models import Video, Season, TVShow

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'  # Serialize all fields of the Video model

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'  # Serialize all fields of the Season model        

class TVShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = '__all__'  # Serialize all fields of the TVShow model                