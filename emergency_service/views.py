from django.http import HttpResponse
from emergency_service import models
from django.shortcuts import render

def len_appeal(request):
    len_appeal = models.Appeal.objects.count()
    return HttpResponse(len_appeal)
