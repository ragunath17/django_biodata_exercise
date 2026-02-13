import django_filters
from bio_data.models import BioData

class BiodataFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    job_title = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = BioData
        fields = ['first_name', 'last_name', 'job_title', 'email', 'city']