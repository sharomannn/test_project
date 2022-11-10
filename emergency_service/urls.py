from django.urls import path
import emergency_service.views
from emergency_service.views import *

from django.views.generic import TemplateView

urlpatterns = [
    path('appeal/add/', emergency_service.views.add_appeal, name='add_appeal'),
    path('applicant/add/', emergency_service.views.add_applicant, name='add_applicant'),
    path('service/add/', emergency_service.views.add_service, name='add_service'),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('service/', EmergencyServicePage.as_view(), name='service'),
    path('applicant/', ApplicantPage.as_view(), name='applicant'),
    path('appeal/', AppealPage.as_view(), name='appeal'),
    path('appeal/<slug:slug>/', AppealOnePage.as_view()),
    path('applicant/<slug:slug>/', ApplicantOnePage.as_view()),


]
