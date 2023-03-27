from django.shortcuts import render, redirect
from core.devmanager.models import DevType
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView
from django.http import JsonResponse
from django.utils.decorators import method_decorator

class DevTypeList(ListView):
    
    model = DevType
    template_name = 'dev_type/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Tipos de Dispositivo'
        return context
    
class DevTypeCreate(CreateView):
    model = DevType
    #form_class =
    
