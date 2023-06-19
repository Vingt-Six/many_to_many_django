from django.db import models

# Create your models here.
class Color(models.Model):
    color = models.CharField(max_length=50)
    def __str__(self):
        return self.color

class Car(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)