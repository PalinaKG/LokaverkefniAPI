from rest_framework import serializers
from .models import emg

class emgSerializer(serializers.ModelSerializer):
    class Meta:
        model = emg
        fields = '__all__'
