from django import forms
from datetime import date
from django.core.exceptions import ValidationError
from emergency_service.models import EmergencyService, Appeal, Applicant


class AddService(forms.ModelForm):
    class Meta:
        model = EmergencyService
        fields = ['name', 'number', 'code']


class AddAppeal(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['applicant'].empty_label = 'Заявитель не выбрана'

    class Meta:
        model = Appeal
        fields = ['status_appeal', 'service', 'applicant', 'number_cases',
                  'not_call']


class AddApplicant(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['photo_applicant', 'surname', 'name', 'name_father', 'gender',
                  'date', 'health_status', 'number', 'slug']

    def clean_number(self):
        nummber = self.cleaned_data['number']
        if len(nummber) > 11:
            raise ValidationError('Длинна больше 11')
        return nummber

    def clean_date(self):
        dt = self.cleaned_data['date']
        if date.today() < dt:
            raise ValidationError('Неправильная дата рождения')
        return dt
