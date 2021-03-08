from rest_framework import serializers
from .models import nausea

class nauseaSerializer(serializers.ModelSerializer):
    class Meta:
        model = nausea
        fields = '__all__'
