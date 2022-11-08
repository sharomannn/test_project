from django.http import HttpResponse
from emergency_service import models
from django.shortcuts import render
from django.views.generic import ListView
from emergency_service.models import EmergencyService, Applicant, Appeal


class EmergencyServicePage(ListView):
    model = EmergencyService
    template_name = 'emergency_service.html'
    context_object_name = 'service_list'


class ApplicantPage(ListView):
    model = Applicant
    template_name = 'applicant.html'
    context_object_name = 'applicant_list'


def applicant_one_page(request, applicant_id):
    context = {
        'applicant': models.Applicant.objects.get(id=applicant_id)
    }
    return render(request, "applicant_one.html", context)


class AppealPage(ListView):
    model = Appeal
    template_name = 'appeal.html'
    context_object_name = 'appeal_list'

def appeal_page(request):
    appeal = models.Appeal.objects.all()
    context = {
        'appeal_list': appeal
    }
    return render(request, 'appeal.html', context)


def appeal_one_page(request, appeal_id):
    context = {
        'appeal': models.Appeal.objects.get(id=appeal_id)
    }
    return render(request, "appeal_one.html", context)


def index_page(request):
    return render(request, 'index.html')


