from django.forms import ModelForm
from app.models import  Employe, Mesure, Charge


class MesureForm(ModelForm):
    class Meta:
        model = Mesure
        fields = '__all__'


class EmployeForm(ModelForm):
    class Meta:
        model = Employe
        fields = '__all__'


class ChargeForm(ModelForm):
    class Meta:
        model = Charge
        fields = '__all__'
