from django.conf.urls import include
from django.db.models import base
from django.urls import path
from rest_framework import routers, urlpatterns

from . import viewsets as listviewsets

route = routers.DefaultRouter()

route.register(r"lists", listviewsets.ListViewSet, basename="Lists")


urlpatterns = [
    #
    path("", include(route.urls))
]
