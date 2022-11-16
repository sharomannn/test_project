from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView
from django_filters.views import FilterView

from emergency_service.filters import ApplicantFilter, AppealFilter
from emergency_service.forms import *


class EmergencyServicePage(ListView):
    model = EmergencyService
    template_name = 'emergency_service.html'
    context_object_name = 'service_list'


# class ApplicantPage(ListView):
#     model = Applicant
#     template_name = 'applicant.html'
#     context_object_name = 'applicant_list'

class ApplicantPageFilter(FilterView):
    model = Applicant
    template_name = 'applicant.html'
    context_object_name = 'applicant_list'
    filterset_class = ApplicantFilter



class ApplicantOnePage(DetailView):
    model = Applicant
    template_name = 'applicant_one.html'


# def applicant_one_page(request, applicant_id):
#     context = {
#         'applicant': models.Applicant.objects.get(id=applicant_id)
#     }
#     return render(request, "applicant_one.html", context)

class AppealPage(FilterView):
    model = Appeal
    template_name = 'appeal.html'
    context_object_name = 'appeal_list'
    filterset_class = AppealFilter

# class AppealPage(ListView):
#     model = Appeal
#     template_name = 'appeal.html'
#     context_object_name = 'appeal_list'


class AppealOnePage(DetailView):
    model = Appeal
    template_name = 'appeal_one.html'


# def appeal_page(request):
#     appeal = models.Appeal.objects.all()
#     context = {
#         'appeal_list': appeal
#     }
#     return render(request, 'appeal.html', context)


# def appeal_one_page(request, appeal_id):
#     context = {
#         'appeal': models.Appeal.objects.get(id=appeal_id)
#     }
#     return render(request, "appeal_one.html", context)


# def index_page(request):
#     return render(request, 'index.html')


class ServiceUpdate(UpdateView):
    model = EmergencyService
    template_name = 'add.html'
    fields = ['name', 'number', 'code']

    def form_valid(self, form):
        try:
            form.save()
            return redirect('/service/')
        except:
            form.add_error()



class AppealUpdate(UpdateView):
    model = Appeal
    template_name = 'add.html'
    fields = ['status_appeal', 'service', 'applicant', 'number_cases',
              'not_call']

    def form_valid(self, form):
        try:
            form.save()
            return redirect('/appeal/')
        except:
            form.add_error()


class ApplicantUpdate(UpdateView):
    model = Applicant
    template_name = 'add.html'
    fields = ['photo_applicant', 'surname', 'name', 'name_father', 'gender',
              'date', 'health_status', 'number', 'slug']

    def form_valid(self, form):
        try:
            form.save()
            return redirect('/applicant/')
        except:
            form.add_error()

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
