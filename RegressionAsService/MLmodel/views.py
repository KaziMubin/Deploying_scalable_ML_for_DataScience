from django.shortcuts import render
from .models import Trainingdata
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import TrainerSerializer


# Create your views here.
class TrainingModel(APIView):
    def get(self, request):
        data = Trainingdata.objects.all()
        serializer = TrainerSerializer(data, many=True)
        return Response(serializer.data)


