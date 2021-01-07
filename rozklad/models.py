from django.db import models

# Create your models here.
from django.utils import timezone
import datetime 

# rozklad
class Tweek(models.Model):
    w_name = models.CharField(max_length=200)

    def __str__(self):
        return self.w_name


class Tlessons(models.Model):
    l_name = models.CharField(max_length=200)

    def __str__(self):
        return self.l_name


class Trozklad(models.Model):
    idweek = models.ForeignKey('Tweek', on_delete=models.CASCADE)
    idlessons = models.ForeignKey('Tlessons', on_delete=models.CASCADE)
    nlesson = models.IntegerField()



class Trozporyadok(models.Model):
    time_start = models.TimeField(default=datetime.time(0, 0), max_length=200)
    time_end = models.TimeField(default=datetime.time(0, 0), max_length=200)
    podiya = models.CharField(max_length=200)

class Urtimes(models.Model):
    time_start = models.TimeField(max_length=200)
    time_end = models.TimeField(max_length=200)
