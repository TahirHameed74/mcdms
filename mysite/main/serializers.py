from rest_framework import serializers

from main.helpers import encrypt_text
from .models import *


class carParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = carParameters
        fields = "__all__"


class houseParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = houseParameters
        fields = "__all__"


