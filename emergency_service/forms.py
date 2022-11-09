from django import forms
from emergency_service.models import EmergencyService, Appeal, Applicant


class AddService(forms.ModelForm):
    class Meta:
        model = EmergencyService
        fields = ['name', 'number', 'code']

class AddAppeal(forms.ModelForm):
    class Meta:
        model = Appeal
        fields = ['status_appeal', 'service', 'applicant', 'number_cases', 'not_call']


class AddApplicant(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['photo_applicant', 'surname', 'name', 'name_father', 'gender', 'date', 'health_status', 'number']