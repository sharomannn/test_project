from django.urls import path
import emergency_service.views

urlpatterns = [
    path('', emergency_service.views.len_appeal),
    path('service', emergency_service.views.emergency_service_page),
    path('applicant', emergency_service.views.applicant_page),
    path('appeal', emergency_service.views.appeal_page),
]
