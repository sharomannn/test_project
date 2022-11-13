from django.urls import path
import emergency_service.views
from emergency_service.views import *

from django.views.generic import TemplateView

urlpatterns = [

    path('qs/number/<int:number>', emergency_service.views.vievs_number),
    path('qs/<int:id>/', emergency_service.views.vievs_id),
    path('qs/len/', emergency_service.views.vievs_len),
    path('qs/rd/', emergency_service.views.redirectd),
    path('qs/', emergency_service.views.vievs),

    path('appeal/add/', emergency_service.views.add_appeal, name='add_appeal'),
    path('applicant/add/', emergency_service.views.add_applicant, name='add_applicant'),
    path('service/add/', emergency_service.views.add_service, name='add_service'),

    path('service/<int:pk>/update', ServiceUpdate.as_view()),
    path('appeal/<slug:slug>/update', AppealUpdate.as_view()),
    path('applicant/<slug:slug>/update', ApplicantUpdate.as_view()),

    path('appeal/<slug:slug>/', AppealOnePage.as_view()),
    path('applicant/<slug:slug>/', ApplicantOnePage.as_view()),

    path('service/', EmergencyServicePage.as_view(), name='service'),
    path('applicant/', ApplicantPageFilter.as_view(), name='applicant'),
    path('appeal/', AppealPage.as_view(), name='appeal'),

    path('', TemplateView.as_view(template_name="index.html"), name='index'),

]
