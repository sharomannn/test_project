from django.http import JsonResponse
from django.shortcuts import render, redirect
from emergency_service.forms import *


def applicant_one_page(request, applicant_id):
    context = {
        'applicant': Applicant.objects.get(id=applicant_id)
    }
    return render(request, "applicant_one.html", context)


def appeal_page(request):
    appeal = Appeal.objects.all()
    context = {
        'appeal_list': appeal
    }
    return render(request, 'appeal.html', context)


def appeal_one_page(request, appeal_id):
    context = {
        'appeal': Appeal.objects.get(id=appeal_id)
    }
    return render(request, "appeal_one.html", context)


def index_page(request):
    return render(request, 'index.html')



def add_service(request):
    form = AddService()
    if request.method == 'POST':
        form = AddService(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error()
    context = {
        'form': form
    }
    return render(request, 'add.html', context)


def add_appeal(request):
    form = AddAppeal()
    if request.method == 'POST':
        form = AddAppeal(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error()
    context = {
        'form': form
    }
    return render(request, 'add.html', context)


def add_applicant(request):
    form = AddApplicant()
    if request.method == 'POST':
        form = AddApplicant(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error()
    context = {
        'form': form
    }
    return render(request, 'add.html', context)


# Отображает всех заявителей
def vievs(request):
    object_list = []
    for p in Applicant.objects.all():
        object_list.append({
            'id': p.pk,
            'number': p.number
        })
    return JsonResponse({'object_list': object_list})

# Отображает сколько всего заявлений
def vievs_len(request):
    qs = Applicant.objects.count()
    return JsonResponse({'result': qs})

# Отображает заявителей по номеру
def vievs_number(request, number):
    qs = Applicant.objects.get(number=number)
    detail = {
        'id': qs.id,
        'name': qs.number
    }
    return JsonResponse({'result': detail})

# Отображает заявителей по id
def vievs_id(request, id):
    qs = Applicant.objects.get(id=id)
    detail = {
        'id': qs.id,
        'Фамилия': qs.surname,
        'Имя': qs.name,
        'Отчество': qs.name_father,
        'Пол': qs.gender,
        'Дата рождения': qs.date,
        'Состояние здоровья': qs.health_status,
        'name': qs.number,
    }
    return JsonResponse({'result': detail})


def redirectd(request):
    response = redirect('http://127.0.0.1:8000')
    return response