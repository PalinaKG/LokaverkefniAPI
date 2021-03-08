from rest_framework import serializers
from .models import spo2

class spo2Serializer(serializers.ModelSerializer):
    class Meta:
        model = spo2
        fields = '__all__'
