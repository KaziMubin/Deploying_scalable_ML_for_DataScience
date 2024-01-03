from rest_framework import serializers
from .models import Trainingdata


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainingdata
        field = "__all__"

