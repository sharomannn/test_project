from django.urls import path
import emergency_service.views
from emergency_service.views import EmergencyServicePage, ApplicantPage, AppealPage


from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('service', EmergencyServicePage.as_view()),
    path('applicant', ApplicantPage.as_view()),
    path('appeal', AppealPage.as_view()),
    path('appeal/<int:appeal_id>', emergency_service.views.appeal_one_page),
    path('applicant/<int:applicant_id>', emergency_service.views.applicant_one_page),
]
