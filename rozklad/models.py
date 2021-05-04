from django.db import models

# Create your models here.
from django.utils import timezone
import datetime 

# rozklad
class Tweek(models.Model):
    w_name = models.CharField(max_length=200)

    def __str__(self):
        return self.w_name



class Teacher(models.Model):
    t_name = models.CharField(max_length=200)

    def __str__(self):
        return self.t_name

class Classroom(models.Model):
    c_name = models.CharField(max_length=200)

    def __str__(self):
        return self.c_name
        


class Tlessons(models.Model):
    teacher_name = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    classroom_name = models.ForeignKey('Classroom', on_delete=models.CASCADE)
    
    l_name = models.CharField(max_length=200)

    def __str__(self):
        return self.l_name


class Trozklad(models.Model):
    idweek = models.ForeignKey('Tweek', on_delete=models.CASCADE)
    idlessons = models.ForeignKey('Tlessons', on_delete=models.CASCADE)
    nomer = models.ForeignKey('Urtimes', on_delete=models.CASCADE)


class other_group_rozklad(models.Model):
    idweek = models.ForeignKey('Tweek', on_delete=models.CASCADE)
    idlessons = models.ForeignKey('Tlessons', on_delete=models.CASCADE)
    nomer = models.ForeignKey('Urtimes', on_delete=models.CASCADE)




class Trozporyadok(models.Model):
    time_start = models.TimeField(default=datetime.time(0, 0), max_length=200)
    time_end = models.TimeField(default=datetime.time(0, 0), max_length=200)
    podiya = models.CharField(max_length=200)

class Urtimes(models.Model):
    time_start = models.TimeField(max_length=200)
    time_end = models.TimeField(max_length=200)
    nur = models.IntegerField()

    def __str__(self):
        return str(self.nur)