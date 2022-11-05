from rest_framework import viewsets
from rest_framework import permissions as p
from rest_framework.viewsets import ModelViewSet
from .serializers import SongSerializer

from .models import SongAPIModel




class SongList(ModelViewSet):
    queryset=SongAPIModel.objects.all()
    serializer_class = SongSerializer
    # permission_classes = [p.DjangoModelPermissions]
     

