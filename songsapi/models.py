from django.db import models

# Create your models here.

class SongAPIModel(models.Model):
    name = models.CharField(max_length = 150)
    artist = models.CharField(max_length = 150, default='Unknown Artist')
    created = models.DateTimeField( auto_now_add=True,blank=True, null=True)
    updated = models.DateTimeField( auto_now=True)

    class Meta:
        ordering = ('-created', )
    def __str__(self):
        return self.name
    
    