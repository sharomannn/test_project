from django.contrib import admin
from emergency_service import models





@admin.register(models.EmergencyService)
class EmergencyService(admin.ModelAdmin):
    list_display = ('name', 'code')


@admin.register(models.Applicant)
class Applicant(admin.ModelAdmin):
    search_fields = ('surname', 'name', 'name_father', 'date')
    list_display = ('surname', 'name', 'name_father', 'number', 'date')
    prepopulated_fields = {"slug": ('surname', 'name','name_father','number',)}




@admin.register(models.Appeal)
class Appeal(admin.ModelAdmin):
    ordering = ('-date',)
    date_hierarchy = 'date'
    list_display_links = ('date', 'number')
    list_filter = ('date', 'status_appeal')
    list_display = ('date', 'number', 'applicant')
    filter_horizontal = ('service',)
