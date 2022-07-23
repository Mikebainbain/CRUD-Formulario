from django import forms
from Models.CRUD.models import Empleado

class formularioEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        