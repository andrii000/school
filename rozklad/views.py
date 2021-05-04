from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Trozklad, Tlessons, Tweek, Trozporyadok, Urtimes, Teacher, Classroom, other_group_rozklad
# from .forms import RozkladForm, RozporyadokForm, UrtimesForm
import datetime
from itertools import chain


def main_menu(request):
    return render(request, 'rozklad/main_menu.html', {})


def all_rozklad(request):

    now_wday = datetime.datetime.today().weekday() + 1


    uroki_list = Trozklad.objects.all()
    uroki_list = uroki_list.order_by('idweek', 'nomer')

    new_ur_list = []
    tabs = []

    o_group_list = other_group_rozklad.objects.all()

    day = 1
    while day <= 6:
        d_ur_list = uroki_list.filter(idweek = day)
        d_o_list = o_group_list.filter(idweek = day)

        count = 0


        for ur in d_ur_list:
            for el in d_o_list:
                if ur.nomer.nur == el.nomer.nur:
                    ur.idlessons.l_name = str(ur.idlessons.l_name) + ' | ' + str(el.idlessons.l_name)
                    count = count + 1


            new_ur_list.append(create_list(ur))

        if count < len(d_o_list):
            temp = 1
            for el in d_o_list:
                if temp > count:
                    el.idlessons.l_name = '... | ' + str(el.idlessons.l_name)
                    new_ur_list.append(create_list(el))
                temp = temp + 1
                    

        tabs.append(new_ur_list)
        new_ur_list = []

        day = day + 1




    all_list = Trozklad.objects.all()
    all_list = all_list.order_by('idweek', 'nomer')



    return render(request, 'rozklad/all_rozklad.html', {
        'tabs': tabs,
        })



class create_list(object):
    """docstring for create_list"""
    def __init__(self, el):
        super(create_list, self).__init__()
        self.l_number = el.nomer.nur
        self.day = el.idweek.w_name
        self.time_start = el.nomer.time_start
        self.time_end = el.nomer.time_end
        self.l_name = el.idlessons
        self.l_date = self.find_next(str(self.l_name))
        self.teacher_name = el.idlessons.teacher_name
        self.classroom_name = el.idlessons.classroom_name
        self.ends_in = ''
        self.ends_in = datetime.datetime.combine(datetime.date(1, 1, 1), self.time_end) - datetime.datetime.combine(datetime.date(1, 1, 1), datetime.datetime.today().time())
        self.ends_in = str(self.ends_in)
        self.ends_in = self.ends_in[2] + self.ends_in[3] + 'хв. до кінця'

    def find_next(self, les):
        self.count = -1
        self.rez_s = ''
        self.closed = 13

        self.all_list = Trozklad.objects.all()
        self.all_list = self.all_list.order_by('idweek', 'nomer')

        for ls in self.all_list :
            if ls.idlessons.l_name == les:
                if self.count == -1:
                    self.count = 1
                    prev_day = ls.idweek.w_name
                    self.closed = 0

                elif ls.idweek.w_name == prev_day:
                    self.count = self.count + 1
                    self.closed = 0

                elif ls.idweek.w_name != prev_day:
                    self.rez_s = self.rez_s + str(prev_day) + '(' + str(self.count) + ') '
                    self.closed = 1
                    self.count = 1
                    prev_day = ls.idweek.w_name

        if self.closed == 0:
            self.rez_s = self.rez_s + str(prev_day) + '(' + str(self.count) + ')'

        return self.rez_s



        
        


def rozklad(request):

    now_wday = datetime.datetime.today().weekday() + 1


    uroki_list = Trozklad.objects.all()
    uroki_list = uroki_list.order_by('idweek', 'nomer')

    new_ur_list = []

    o_group_list = other_group_rozklad.objects.all()

    # day = 1
    # while day <= 6:
    #     d_ur_list = uroki_list.filter(idweek = day)
    #     d_o_list = o_group_list.filter(idweek = day)


    #     for ur in d_ur_list:
    #         for el in d_o_list:
    #             if ur.nomer.nur == el.nomer.nur:
    #                 ur.idlessons.l_name = str(ur.idlessons.l_name) + ' | ' + str(el.idlessons.l_name)

    #         new_ur_list.append(create_list(ur))

    #     day = day + 1



    d_ur_list = uroki_list.filter(idweek = int(now_wday))
    d_o_list = o_group_list.filter(idweek = int(now_wday))


    count = 0

    for ur in d_ur_list:
        for el in d_o_list:
            if ur.nomer.nur == el.nomer.nur:
                ur.idlessons.l_name = str(ur.idlessons.l_name) + ' | ' + str(el.idlessons.l_name)
                count = count + 1

        new_ur_list.append(create_list(ur))

    if count < len(d_o_list):
        temp = 1
        for el in d_o_list:
            if temp > count:
                el.idlessons.l_name = '... | ' + str(el.idlessons.l_name)
                new_ur_list.append(create_list(el))
            temp = temp + 1






    rozporyadok_list = Trozporyadok.objects.all()



    # now_wday = datetime.datetime.today().weekday() + 1

    now_time = datetime.datetime.today().time()

    # now_wday = int(now_wday)
    if now_wday == 7:
        uroki_list = uroki_list.filter(idweek = 1)

    temp = 1
    while temp <= 6:
        if now_wday == temp:
            uroki_list = uroki_list.filter(idweek = temp)
        temp = temp + 1


    # uroki_list = uroki_list.filter(idweek = now_wday)
    


    all_list = Trozklad.objects.all()
    all_list = all_list.order_by('idweek', 'nomer')


    urtimes_list = Urtimes.objects.all()
    urtimes_list = urtimes_list.order_by('time_start')
    
    # rez_list = sorted(chain(uroki_list, urtimes_list),key=lambda instance: instance.id, reverse=False)




    les_list = Tlessons.objects.all()

    next_dict = {}
    # next_dict['name']='Nick'


    tab_list_before = []
    tab_list_now = []
    tab_list_after = []

    def now_les(time):
        for el in new_ur_list:
            if el.time_start <= time:
                if el.time_end >= time:
                    return el.l_number
        return -1

    now_l = now_les(now_time)


    for el in new_ur_list:
        week_day = el.day
        if el.l_number < now_l:
            tab_list_before.append(el)

    for el in new_ur_list:
        if el.l_number == now_l:
            tab_list_now.append(el)

    for el in new_ur_list:
        if el.l_number > now_l:
            tab_list_after.append(el)



    return render(request, 'rozklad/rozklad.html', {
        'uroki_list': uroki_list,
        'rozporyadok_list': rozporyadok_list,
        'now_wday': now_wday,
        'urtimes_list': urtimes_list,
        'all_list': all_list,
        # 'find_next': find_next,
        # 'next_dict': next_dict,
        'tab_list_before': tab_list_before,
        'tab_list_now': tab_list_now,
        'tab_list_after': tab_list_after,
        'now_l': now_l,
        'week_day': week_day,
        'new_ur_list': new_ur_list,


        })  

def rozklad_edit(request):

    # if request.method == "POST":
    #     form = RozkladForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()

    # else:
    #     form = RozkladForm()

    # doc_list = Trozklad.objects.all()
    # doc_list = doc_list.order_by('idweek', 'nomer')

    # if request.method == "POST":
    #     form_2 = RozporyadokForm(request.POST, request.FILES)
    #     if form_2.is_valid():
    #         form_2.save()

    # else:
    #     form_2 = RozporyadokForm()

    # doc_list_2 = Trozporyadok.objects.all()

    # if request.method == "POST":
    #     form_3 = UrtimesForm(request.POST, request.FILES)
    #     if form_3.is_valid():
    #         form_3.save()

    # else:
    #     form_3 = UrtimesForm()

    # doc_list_3 = Urtimes.objects.all()
    return render(request, 'rozklad/rozklad_edit.html', {
        # 'form': form,
        # 'doc_list': doc_list,
        # 'doc_list_2': doc_list_2,
        # 'form_2': form_2,
        # 'doc_list_3': doc_list_3,
        # 'form_3': form_3,
        })  