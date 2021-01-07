from django.contrib import admin

# Register your models here.
from .models import Tweek, Trozklad, Tlessons, Trozporyadok, Urtimes

class TweekAdmin(admin.ModelAdmin):
    list_display = ('w_name',)

admin.site.register(Tweek, TweekAdmin)

class TlessonsAdmin(admin.ModelAdmin):
    list_display = ('l_name',)

admin.site.register(Tlessons, TlessonsAdmin)

class TrozporyadokAdmin(admin.ModelAdmin):
    list_display = ('time_start', 'time_end', 'podiya')

admin.site.register(Trozporyadok, TrozporyadokAdmin)

class UrtimesAdmin(admin.ModelAdmin):
    list_display = ('time_start', 'time_end')

admin.site.register(Urtimes, UrtimesAdmin)