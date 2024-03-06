from django.shortcuts import render
from .serializers import MovieSerializer
from rest_framework import viewsets
from .models import Moviedata
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset=Moviedata.objects.all()
    serializer_class=MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset=Moviedata.objects.filter(typ='action')
    serializer_class=MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset=Moviedata.objects.filter(typ='Comedy')
    serializer_class=MovieSerializer



