from django.shortcuts import render
from rest_framework import viewsets
from .models import programmer
from .serializers import programmerSerializer
from .serializers import studentSerializer
from .models import student

# Create your views here.
class ProgrammerViewset(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = programmerSerializer


class studentViewset(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class= studentSerializer