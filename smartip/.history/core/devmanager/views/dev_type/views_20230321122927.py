from django.shortcuts import render
from core.devmanager.models import DevType

def dev_type_list(request):
    
    data = {
        'title': 'Listado de Tipos de Disositivo'
    }
    return render(request, 'dev_type/list.html', data)