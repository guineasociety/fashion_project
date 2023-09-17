import django_filters
from .models import Employe, Mesure


class MesureFilter(django_filters.FilterSet):
    class Meta:
        model = Mesure
        fields = ['code','nom','date_rdv']


class EmployeFilter(django_filters.FilterSet):
    class Meta:
        model = Employe
        fields = ['contact_employe', 'nom_employe']
