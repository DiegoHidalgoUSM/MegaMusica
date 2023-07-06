from rest_framework import serializers
from .models import Disco

class DiscoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disco
        fields = '__all__'