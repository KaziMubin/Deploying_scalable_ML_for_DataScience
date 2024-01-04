from django.contrib import admin
from django.urls import path
from .views import TrainingModel, InputTrainingData

urlpatterns = [
    path("training/", TrainingModel.as_view()),
    path("entrydata/", InputTrainingData.as_view())
]
