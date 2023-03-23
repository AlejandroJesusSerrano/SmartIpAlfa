from django.shortcuts import render
from .models import DevType

# Create your views here.
def myfirstview(request):
    data = {
        'name': 'Alejandro', 
        'Tipo de Dispositivo': DevType.objects.all()
    }

    return render(request, 'index.html', data)
