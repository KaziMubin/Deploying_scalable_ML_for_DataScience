from django.db import models

# Create your models here.
class Trainingdata(models.Model):
    Xtraining = models.IntegerField()
    ylabels = models.IntegerField()
    user = models.CharField(max_length=100)

    def __str__(self):
        print(self.user, self.Xtraining, self.ylabels)


{
    "Xtraining" : [100,200,300,400,500,600,700,800,900],
    "ylabels" : [911,811,711,611,511,411,311,211,111],
    "user" : "Mubin"
}

{
    "user" : "Mubin"
}