from django.urls import path
import emergency_service.views
from emergency_service.views import *


from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('service', EmergencyServicePage.as_view()),
    path('applicant', ApplicantPage.as_view()),
    path('appeal', AppealPage.as_view()),
    path('appeal/<slug:slug>', AppealOnePage.as_view()),
    path('applicant/<slug:slug>', ApplicantOnePage.as_view()),
]
