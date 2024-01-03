from django.contrib import admin
from django.urls import path
from .views import TrainingModel

urlpatterns = [
    path("training/", TrainingModel.as_view()),
]
