from django.db import models


class Video(models.Model):
    VIDEO_TYPES = (
        ('Movie', 'Movie'),
        ('Clip', 'Clip'),
        ('Episode', 'Episode'),
    )
    
    video_type = models.CharField(max_length=10, choices=VIDEO_TYPES)
    creation_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)  # Automatically set to the creation date
    title = models.CharField(max_length=255)
    season = models.ForeignKey('Season', on_delete=models.CASCADE, null=True, blank=True) # Season. Can be null for movies and clips    
    tv_show = models.ForeignKey('TVShow', on_delete=models.CASCADE, null=True, blank=True) # TVShow. Can be null for movies and clips    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        
        first_save = not self.pk
        super(Video, self).save(*args, **kwargs)    
        
        # Update the tv_show field with the creation_date of the last video
        if (first_save) and (self.tv_show):
            try:
                tv_show = TVShow.objects.get(id=self.tv_show.id)
                if tv_show:
                    tv_show.last_episode_creation_datetime = self.creation_datetime
                    tv_show.save()
            except TVShow.DoesNotExist:
                # Handle the case where the TVShow with the given ID does not exist
                pass
        

class Season(models.Model):
    title = models.CharField(max_length=255)
    tv_show = models.ForeignKey('TVShow', on_delete=models.CASCADE, null=True, blank=True) # TVShow. Can be null for movies and clips    

    def __str__(self):
        return self.title
    

class TVShow(models.Model):
    title = models.CharField(max_length=255)
    last_episode_creation_datetime = models.DateTimeField(null=True, blank=True) 

    def __str__(self):
        return self.title    