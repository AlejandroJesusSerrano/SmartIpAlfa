from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from core.devmanager.forms import DevTypeForm
from core.devmanager.models import DevType

class DevTypeList(ListView):
    
    model = DevType
    template_name = 'dev_type/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Tipos de Dispositivo'
        return context
    
class DevTypeCreate(CreateView):
    model = DevType
    form_class = DevTypeForm
    template_name = 'dev_type/create.html'
    success_url = reverse_lazy('core:type_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Agregar Nuevo Tipo de Dispositivo'
        return context
    

