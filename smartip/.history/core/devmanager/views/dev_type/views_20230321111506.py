from django.shortcuts import render

def dev_type_list(request):
    data = {
        
    }
    return render(request, 'dev_type/list.html', data)