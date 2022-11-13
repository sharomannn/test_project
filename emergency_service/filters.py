import django_filters

from emergency_service.models import Applicant


class ApplicantFilter(django_filters.FilterSet):
    date = django_filters.CharFilter(label='Дата рождения', lookup_expr='contains')
    number = django_filters.CharFilter(label='Номер телефона', lookup_expr='contains')
    surname = django_filters.CharFilter(label='Фамилия', lookup_expr='contains')
    name = django_filters.CharFilter(label='Имя', lookup_expr='contains')
    name_father = django_filters.CharFilter(label='Отчество', lookup_expr='contains')

    class Meta:
        model = Applicant
        fields = ['surname', 'name', 'name_father', 'date', 'number', ]
