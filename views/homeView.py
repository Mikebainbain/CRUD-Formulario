from django.http import HttpResponse
from django.template.loader import get_template


class HomeView():
    def home(self):
        
        plantilla = get_template('index.html')
        return HttpResponse(plantilla.render()) 
    
    def usuario(self):
        return HttpResponse('Pagina del empleado')

    def formulario(request):
        plantilla = get_template('form.html')
        return HttpResponse(plantilla.render())