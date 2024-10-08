from django.db import models
2
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
# Create your models here.
