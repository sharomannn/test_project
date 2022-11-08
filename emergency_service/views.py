from django.http import HttpResponse
from emergency_service import models
from django.shortcuts import render
import datetime


def len_appeal(request):
    len_appeal = models.Appeal.objects.count()
    return HttpResponse(len_appeal)


def emergency_service_page(request):
    service = models.EmergencyService.objects.all()
    context = {
        'service_list': service
    }
    return render(request, 'emergency_service.html', context)


def applicant_page(request):
    applicant = models.Applicant.objects.all()
    context = {
        'applicant_list': applicant
    }
    return render(request, 'applicant.html', context)

def applicant_one_page(request, applicant_id):
    context = {
        'applicant': models.Applicant.objects.get(id=applicant_id)
    }
    return render(request, "applicant_one.html", context)


def appeal_page(request):
    appeal = models.Appeal.objects.all()
    now = datetime.datetime.now()
    context = {
        'now': now,
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


