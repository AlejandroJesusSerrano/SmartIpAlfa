from django.urls import path
from core.devmanager.views.dev_type.views import DevTypeList, DevTypeCreate

app_name = 'core'

urlpatterns = [
    path('dev_type/list/', DevTypeList.as_view(), name='DevTypeList'),
    path('dev_type/create/', DevTypeCreate.as_view(), name='DevTypeCreate')
]