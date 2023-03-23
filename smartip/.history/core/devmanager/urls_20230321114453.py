from django.urls import path
from core.devmanager.views.dev_type.views import dev_type_list

app_name = 'core'

urlpatterns = [
    path('dev_type/list/', dev_type_list, name='DevTypeList')
]