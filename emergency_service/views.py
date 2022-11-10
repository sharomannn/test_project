from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from emergency_service.models import *
from emergency_service.forms import *


class EmergencyServicePage(ListView):
    model = EmergencyService
    template_name = 'emergency_service.html'
    context_object_name = 'service_list'


class ApplicantPage(ListView):
    model = Applicant
    template_name = 'applicant.html'
    context_object_name = 'applicant_list'


class ApplicantOnePage(DetailView):
    model = Applicant
    template_name = 'applicant_one.html'


# def applicant_one_page(request, applicant_id):
#     context = {
#         'applicant': models.Applicant.objects.get(id=applicant_id)
#     }
#     return render(request, "applicant_one.html", context)


class AppealPage(ListView):
    model = Appeal
    template_name = 'appeal.html'
    context_object_name = 'appeal_list'


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
    return render(request, 'add .html', context)


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
