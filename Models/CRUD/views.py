from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpRequest
from Models.CRUD.forms import formularioEmpleado
from Models.CRUD.models import Empleado

from Models.CRUD.forms import formularioEmpleado

# Create your views here.
<<<<<<< HEAD
class FormularioEmpleadoView(): #Metodos para registar empleados
    def index(request):                 
        empleado = formularioEmpleado()
        return render(request,"Empleadoindex.html",{"formulario":empleado} )
    
    def procesar_formulario(request):
        empleado = formularioEmpleado(request.POST)
        if empleado.is_valid():
            empleado.save()
            empleado = formularioEmpleado()
        return render(request, "Empleadoindex.html", {"formulario": empleado, "mensaje": 'OK'})

    def listar_empleados(request):# Metodo que muestra toda la tabla listad e empleados
        empleados = Empleado.objects.all()
        return render(request, "ListaEmpleados.html",{"empleados":empleados})
    
    def edit(request, idempleado):
        empleado = Empleado.objects.filter(id=idempleado).first()
        form = formularioEmpleado(instance=empleado)
        return render(request, "EmpleadoEdit.html", {"formulario":form, 'empleado':empleado})



    
