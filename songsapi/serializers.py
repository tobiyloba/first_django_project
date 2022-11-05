from rest_framework import serializers
from .models import SongAPIModel

class SongSerializer(serializers.ModelSerializer):


    class Meta:
        model=SongAPIModel
        fields= '__all__'
