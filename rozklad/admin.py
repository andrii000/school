from django.contrib import admin

# Register your models here.
from .models import Tweek, Trozklad, Tlessons, Trozporyadok, Urtimes, Classroom, Teacher, other_group_rozklad

class TweekAdmin(admin.ModelAdmin):
    list_display = ('w_name',)

admin.site.register(Tweek, TweekAdmin)

class TlessonsAdmin(admin.ModelAdmin):
    list_display = ('l_name', 'teacher_name', 'classroom_name')

admin.site.register(Tlessons, TlessonsAdmin)



class TeacherAdmin(admin.ModelAdmin):
    list_display = ('t_name',)

admin.site.register(Teacher, TeacherAdmin)

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('c_name',)

admin.site.register(Classroom, ClassroomAdmin)



class TrozporyadokAdmin(admin.ModelAdmin):
    list_display = ('time_start', 'time_end', 'podiya')

admin.site.register(Trozporyadok, TrozporyadokAdmin)

class TrozkladAdmin(admin.ModelAdmin):
    list_display = ('idweek', 'idlessons', 'nomer')

admin.site.register(Trozklad, TrozkladAdmin)

class UrtimesAdmin(admin.ModelAdmin):
    list_display = ('time_start', 'time_end')

admin.site.register(Urtimes, UrtimesAdmin)


class other_group_rozkladAdmin(admin.ModelAdmin):
    list_display = ('idweek', 'idlessons', 'nomer')

admin.site.register(other_group_rozklad, other_group_rozkladAdmin)