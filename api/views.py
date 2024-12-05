from django.shortcuts import render
from rest_framework import viewsets
from .models import programmer
from .serializers import programmerSerializer

# Create your views here.
class ProgrammerViewset(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = programmerSerializer