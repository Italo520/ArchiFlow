from rest_framework import serializers
from .models import Projeto

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'