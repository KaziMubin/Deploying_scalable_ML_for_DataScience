from django.shortcuts import render
from .models import Trainingdata
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import TrainerSerializer
from rest_framework import status


# Create your views here.
############### get input data

class InputTrainingData(APIView):
    def post(self, request):
        trainingdata = request.data['Xtraining']
        traininglabels = request.data['ylabels']

        if len(traininglabels) == len(trainingdata):
            for (i, j) in zip(trainingdata, traininglabels):
                serializer = TrainerSerializer(data={"Xtraining": i,
                                                     "ylabels": j,
                                                     "user": request.data['user']})
                if serializer.is_valid():
                    serializer.save()
                    if i == len(trainingdata):
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
            return Response("Data added", status=status.HTTP_201_CREATED)
        else:
            return Response("Miss data and labels length missmatch")

############# show result

class TrainingModel(APIView):
    def get(self, request):
        data = Trainingdata.objects.all()
        serializer = TrainerSerializer(data, many=True)
        print(serializer.data[4]['user'])
        print('#####################')
        return Response(serializer.data)




