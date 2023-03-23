from django.urls import path
from .views import myfirstview

urlpatterns = [
    path('uno/', myfirstview, name='Primera')
]