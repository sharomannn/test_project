from django.contrib import admin
from emergency_service import models
from emergency_service.models import Appeal


@admin.register(models.EmergencyService)
class EmergencyServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


@admin.register(models.Appeal)
class AppealAdmin(admin.ModelAdmin):
    fields = ('applicant', 'status_appeal', 'service', 'number_cases',
              'not_call')  # Настройка отображения
    ordering = ('-date',)
    list_display_links = ('date', 'number')
    list_filter = ('date', 'status_appeal')
    list_display = ('date', 'number', 'applicant')
    filter_horizontal = ('service',)


class AppealInline(admin.StackedInline):
    model = Appeal
    extra = 1


@admin.register(models.Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    exclude = ('gender', )
    # readonly_fields =
    search_fields = ('surname', 'name', 'name_father', 'date')  # Поиск
    list_display = ('surname', 'name', 'name_father', 'number', 'date')
    prepopulated_fields = {
        "slug": ('surname', 'name', 'name_father', 'number',)}
    inlines = [AppealInline]
