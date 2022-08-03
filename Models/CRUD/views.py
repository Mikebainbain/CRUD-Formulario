from django.http import HttpRequest
from django.shortcuts import render
from Models.CRUD.forms import formularioEmpleado
from Models.CRUD.models import Empleado
from Models.CRUD.forms import formularioEmpleado
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class FormularioEmpleadoView(): # Metodos para registar empleados()
    def index(request):                 
        empleado = formularioEmpleado()
        return render(request,"Empleadoindex.html",{"formulario":empleado} )
    
    def procesar_formulario(request):# Metodo que valida si los datos introducidos en el formulario son validos y los guarda
        empleado = formularioEmpleado(request.POST)
        if empleado.is_valid():
            empleado.save()
            empleado = formularioEmpleado()
        return render(request, "Empleadoindex.html", {"formulario": empleado, "mensaje": 'OK'})

    def listar_empleados(request):# Metodo que muestra toda la tabla lista de empleados
        empleados = Empleado.objects.all()
        return render(request, "ListaEmpleados.html",{"empleadox":empleados})
    
    def edit(request, idempleado):
        empleado = Empleado.objects.filter(idempleado=idempleado).first()
        form = formularioEmpleado(instance=empleado)
        return render(request, "EmpleadoEdit.html", {"formulario":form, 'empleado':empleado})
    
    def actualizar_empleado(request, idempleado):
        empleado = Empleado.objects.get(pk = idempleado)
        forms = formularioEmpleado(request.POST, instance=empleado)
        if forms.is_valid():
            forms.save()
        empleados = Empleado.objects.all()
        return render(request, "ListaEmpleados.html",{"empleados":empleados})

    def borrar(request, idempleado):
        empleado = Empleado.objects.get (pk = idempleado)
        empleado.delete()
        empleados = Empleado.objects.all()
        return render(request, "ListaEmpleados.html",{"empleados":empleados, "mensaje": 'OK'})

    def empleado(request):
         return render(request, "Empleado.html")    



# PARA HACER EL FORMULARIO DE REGISTRO

    def register(request):
        if request.method == 'POST':
            form =  UserCreationForm(request.POST)
            if forms.is_valid():
                username=form.cleaned_data['username']
                messages.success(request, f'Usuario {username} creado')
        else:
            form = UserCreationForm()
        return render(request, 'registro.html',{'form':form})

 


    
