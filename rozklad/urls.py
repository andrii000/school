from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('rozklad/', views.rozklad, name='rozklad'),
    path('rozklad/edit', views.rozklad_edit, name='rozklad_edit'),
    path('rozklad/all', views.all_rozklad, name='all_rozklad'),
]