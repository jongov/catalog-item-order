from django.contrib import admin
from .models import Video, Season, TVShow


class VideoAdmin(admin.ModelAdmin):    
    list_display = ('id', 'title', 'video_type', 'season', 'tv_show', 'creation_datetime')
    list_filter = ('video_type',)  # Optional: Add filters for the 'type' field
    search_fields = ('title', 'tv_show')  # Optional: Add search functionality for 'title' and 'tv_show'

admin.site.register(Video, VideoAdmin)


class SeasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tv_show')  # Display 'id' and 'title' fields in the admin list view
    list_filter = ('tv_show',)  # Optional: Add filters for the 'type' field
    search_fields = ('title',)  # Add search functionality for 'title' field

admin.site.register(Season, SeasonAdmin)


class TVShowAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'last_episode_creation_datetime')  # Display 'id' and 'title' fields in the admin list view
    search_fields = ('title',)  # Add search functionality for 'title' field

admin.site.register(TVShow, TVShowAdmin)



