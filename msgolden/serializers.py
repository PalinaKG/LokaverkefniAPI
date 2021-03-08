from rest_framework import serializers
from .models import msgolden

class msgoldenSerializer(serializers.ModelSerializer):
    class Meta:
        model = msgolden
        fields = '__all__'
