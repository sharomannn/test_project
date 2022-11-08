from django.urls import path
import emergency_service.views

urlpatterns = [
    path('', emergency_service.views.index_page),
    path('service', emergency_service.views.emergency_service_page),
    path('applicant', emergency_service.views.applicant_page),
    path('appeal', emergency_service.views.appeal_page),
    path('appeal/<int:appeal_id>', emergency_service.views.appeal_one_page),
    path('applicant/<int:applicant_id>', emergency_service.views.applicant_one_page),
]
