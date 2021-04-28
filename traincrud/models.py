from django.db import models

class PositionStart(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class PositionEnd(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Train(models.Model):
    TrainName = models.CharField(max_length=100)
    TrainNo = models.CharField(max_length=14)
    Start = models.ForeignKey(PositionStart,on_delete=models.CASCADE)
    End = models.ForeignKey(PositionEnd,on_delete=models.CASCADE)
