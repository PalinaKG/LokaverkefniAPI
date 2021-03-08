from rest_framework import serializers
from .models import eeg

class eegSerializer(serializers.ModelSerializer):
    class Meta:
        model = eeg
        fields = '__all__'
