from django.shortcuts import render
from devmanager.models import DevType

def dev_type_list(request):
    list_dev_type = DevType.objects.all
    data = {
        'list_dev_type': 'list_dev_type'
    }
    return render(request, 'dev_type/list.html', data)