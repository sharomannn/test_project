import django_filters

from emergency_service.models import Applicant


class ApplicantFilter(django_filters.FilterSet):
    date = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Applicant
        fields = ['date']