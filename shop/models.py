from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    prix = models.FloatField()
    stock = models.IntegerField()
    category = models.ManyToManyField(Category)