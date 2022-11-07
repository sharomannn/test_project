from django.http import HttpResponse
from emergency_service import models
from django.shortcuts import render

def len_appeal(request):
    len_appeal = models.Appeal.objects.count()
    return HttpResponse(len_appeal)

def emergency_service_page(request):
    service = models.EmergencyService.objects.all()
    return render(request, 'emergency_service.html', context={'service_list':service})

def applicant_page(request):
    applicant = models.Applicant.objects.all()
    return render(request, 'applicant.html', context={'applicant_list':applicant})

def appeal_page(request):
    appeal = models.Appeal.objects.all()
    return render(request, 'appeal.html', context={'appeal_list': appeal})



