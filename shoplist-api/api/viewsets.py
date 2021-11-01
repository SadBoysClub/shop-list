from rest_framework import viewsets
from rest_framework.serializers import Serializer
from api import serializers, models


class ListViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ListSerializer
    queryset = models.List.objects.all()
