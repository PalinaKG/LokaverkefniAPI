from rest_framework import serializers
from .models import hr

class hrSerializer(serializers.ModelSerializer):
    class Meta:
        model = hr
        fields = '__all__'
