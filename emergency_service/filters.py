import django_filters
from django.db.models import Q

from django.db.models import CharField, Value
from django.db.models.functions import Concat

from emergency_service.models import Applicant, Appeal

IN_WORK = 'В работе'
FINNISHED = 'Завершено'
STATUS_CHOICES = (
    (IN_WORK, 'В работе'),
    (FINNISHED, 'Завершено'),)


class ApplicantFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(label='Дата рождения',
                                     lookup_expr='contains')
    number = django_filters.CharFilter(label='Номер телефона',
                                       lookup_expr='contains')
    # surname = django_filters.CharFilter(label='Фамилия', lookup_expr='contains')
    # name = django_filters.CharFilter(label='Имя', lookup_expr='contains')
    # name_father = django_filters.CharFilter(label='Отчество',
    #                                         lookup_expr='contains')
    fio = django_filters.CharFilter(method='my_custom_filter', label="Поиск по ФИО",
                                  lookup_expr='contains')

    def my_custom_filter(self, queryset, name, value):
        return queryset.annotate(
            full_name=Concat(
                'surname', Value(' '), 'name', Value(' '), 'name_father',
                output_field=CharField()
            ),
            name_surname= Concat(
                'surname', Value(' '), 'name',
                output_field=CharField()
            )
        ).filter(Q(name=value, surname=value, name_father=value, full_name=value, name_surname=value, _connector=Q.OR))

    class Meta:
        model = Applicant
        fields = ['fio', 'date', 'number', ]


class AppealFilter(django_filters.FilterSet):
    status_appeal = django_filters.ChoiceFilter(choices=STATUS_CHOICES)
    service = django_filters.AllValuesMultipleFilter(label='Экстренные службы',
                                                     field_name='service__name')
    applicant = django_filters.AllValuesFilter(label='Заявитель',
                                               field_name='applicant__surname')

    class Meta:
        model = Appeal
        fields = ['status_appeal', 'service', 'applicant']
