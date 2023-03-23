from django.shortcuts import render

# Create your views here.
def myfirstview(request):
    data = {
        'name': 'Alejandro'
    }

    return render(request, 'index.html')
