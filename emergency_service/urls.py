from django.urls import path
import emergency_service.views

urlpatterns = [
    path('', emergency_service.views.len_appeal),
]
