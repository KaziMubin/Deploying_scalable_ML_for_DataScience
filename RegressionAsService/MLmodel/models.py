from django.db import models

# Create your models here.
class Trainingdata(models.Model):
    Xtraining = models.IntegerField()
    ylabels = models.IntegerField()
    user = models.CharField(max_length=100)

    def __str__(self):
        print(self.user, self.Xtraining, self.ylabels)