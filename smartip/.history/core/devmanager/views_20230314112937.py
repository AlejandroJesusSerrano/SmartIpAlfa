from django.shortcuts import render
from .models import DevType

# Create your views here.
def myfirstview(request):
    data = {
        'name': 'Alejandro', 
        'dev_type': DevType.objects.all()
    }

    return render(request, 'index.html', data)
