from django import forms
from Models.CRUD.models import Empleado
from django.contrib.auth.forms import UserCreationForm #es un form de django que se utiliza para la autenticacion 
from django.contrib.auth.models import User

class formularioEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_text = {k:"" for k in fields}
