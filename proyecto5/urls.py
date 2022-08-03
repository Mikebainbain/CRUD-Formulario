"""proyecto5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from views.homeView import HomeView
from Models.CRUD.views import FormularioEmpleadoView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.home, name = 'home'),
    path('usuario/',HomeView.usuario, name ='usuario' ),
    path('formulario/',HomeView.formulario, name = 'form'),
    path('registrarEmpleado/', FormularioEmpleadoView.index, name = 'registrarEmpleado'),
    path('guardarEmpleado/', FormularioEmpleadoView.procesar_formulario,name = 'guardarEmpleado'),
    path('listarEmpleados/', FormularioEmpleadoView.listar_empleados,name = 'listarEmpleados'),
    path('editarEmpleado/<int:idempleado>',  FormularioEmpleadoView.edit, name='editarEmpleados'),
    path('actualizarEmpleado/<int:idempleado>',  FormularioEmpleadoView.actualizar_empleado, name='actualizarEmpleados'),
    path('eliminarEmpleados/<int:idempleado>',  FormularioEmpleadoView.borrar, name='eliminarEmpleados'),
    path('empleados/', FormularioEmpleadoView.empleado, name='empleado'),
    path('register/', FormularioEmpleadoView.register, name = 'register'),
    path('login/',LoginView.as_view(template_name='login.html'), name = 'login'),
    path('logout/',LogoutView.as_view(template_name='logout.html'), name = 'logout'),
]