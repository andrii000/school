from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Trozklad, Tweek, Trozporyadok, Urtimes
from .forms import RozkladForm, RozporyadokForm, UrtimesForm
import datetime
from itertools import chain


def main_menu(request):
    return render(request, 'rozklad/main_menu.html', {})


def rozklad(request):
    uroki_list = Trozklad.objects.all()

    rozporyadok_list = Trozporyadok.objects.all()

    now_wday = datetime.datetime.today().weekday() + 1
    uroki_list = uroki_list.filter(idweek = now_wday).order_by('nlesson')

    urtimes_list = Urtimes.objects.all()
    
    rez_list = sorted(chain(uroki_list, urtimes_list),key=lambda instance: instance.id, reverse=False)

    return render(request, 'rozklad/rozklad.html', {
        'uroki_list': uroki_list,
        'rozporyadok_list': rozporyadok_list,
        'now_wday': now_wday,
        'urtimes_list': urtimes_list,
        'rez_list': rez_list,
        })  

def rozklad_edit(request):
    # doc_list = Post.objects.all()

    if request.method == "POST":
        form = RozkladForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # return HttpResponseRedirect('/lsprj/')    
    else:
        form = RozkladForm()

    doc_list = Trozklad.objects.all()

    if request.method == "POST":
        form_2 = RozporyadokForm(request.POST, request.FILES)
        if form_2.is_valid():
            form_2.save()

            # return HttpResponseRedirect('/lsprj/')    
    else:
        form_2 = RozporyadokForm()

    doc_list_2 = Trozporyadok.objects.all()

    if request.method == "POST":
        form_3 = UrtimesForm(request.POST, request.FILES)
        if form_3.is_valid():
            form_3.save()

            # return HttpResponseRedirect('/lsprj/')    
    else:
        form_3 = UrtimesForm()

    doc_list_3 = Urtimes.objects.all()
    return render(request, 'rozklad/rozklad_edit.html', {
        'form': form,
        'doc_list': doc_list,
        'doc_list_2': doc_list_2,
        'form_2': form_2,
        'doc_list_3': doc_list_3,
        'form_3': form_3,
        })  