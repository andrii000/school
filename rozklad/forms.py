from django import forms
from django.forms import  ModelForm, CharField
from .models import Trozklad, Trozporyadok, Urtimes

class RozkladForm(ModelForm):
    class Meta:
        model = Trozklad
        fields = ('idweek','nlesson','idlessons')
        labels = {
		        'idweek': 'День тижня',
                'idlessons': 'Назва уроку',
                'nlesson': 'Номер уроку',
            }

class RozporyadokForm(ModelForm):
    class Meta:
        model = Trozporyadok
        fields = ('time_start','time_end','podiya')
        labels = {
                'time_start': 'Початок події',
                'time_end': 'Кінець події',
                'podiya': 'Назва події',
            }

class UrtimesForm(ModelForm):
    class Meta:
        model = Urtimes
        fields = ('time_start','time_end')
        labels = {
                'time_start': 'Початок уроку',
                'time_end': 'Кінець уроку',
            }