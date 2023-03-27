from django.shortcuts import render
from core.devmanager.models import DevType
from django.views.generic import ListView

def dev_type_list(request):
    
    data = {
        'title': 'Listado de Tipos de Disositivo',
        'dev_type': DevType.objects.all()
    }
    return render(request, 'dev_type/list.html', data)

class DevTypeList(ListView):
    model = DevType
    template_name = 'dev_type/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Tipos de Dispositivo'
        return context