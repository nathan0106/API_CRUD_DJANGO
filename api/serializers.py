from rest_framework import serializers
from .models import programmer

class programmerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = programmer
        fields = '__all__'