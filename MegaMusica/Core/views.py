from django.shortcuts import render
from rest_framework import viewsets
from .serializer import DiscoSerializer
from .models import Disco

# Create your views here.
class DiscoViewSet(viewsets.ModelViewSet):
    queryset=Disco.objects.all()
    serializer_class=DiscoSerializer