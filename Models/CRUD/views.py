from django.http import HttpRequest
from django.shortcuts import render

from Models.CRUD.forms import formularioEmpleado

# Create your views here.
class FormularioView(HttpRequest):
    
    def index(request):
        empleado = formularioEmpleado()
        return render(request, "Empleadoindex.html",{"formulario":empleado})
    
    def procesar_formulario(request):
        empleado = formularioEmpleado()
        if empleado.is_valid():
            empleado.save()
            empleado = formularioEmpleado
        return render(request, "Empleadoindex.html",{"formulario":empleado, "mesanje": 'OK'})
     


