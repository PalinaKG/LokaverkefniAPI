from rest_framework import serializers
from .models import generalinfo

class generalinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = generalinfo
        fields = '__all__'
