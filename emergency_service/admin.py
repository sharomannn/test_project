from django.contrib import admin
from emergency_service import models


@admin.register(models.EmergencyService)
class EmergencyService(admin.ModelAdmin):
    list_display = ('name', 'code')


@admin.register(models.Applicant)
class Applicant(admin.ModelAdmin):
    list_display = ('name', 'number')


@admin.register(models.Appeal)
class Appeal(admin.ModelAdmin):
    list_display = ('date', 'number')
