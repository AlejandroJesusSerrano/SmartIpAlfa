from django.contrib import admin
from core.devmanager.models import DevType, Brand, Model, Ip, Techs, DevStatus, 

# Register your models here.

admin.site.register(DevType)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Ip)
admin.site.register(Techs)
admin.site.register(DevStatus)
admin.site.register(Province)
admin.site.register(Locality)
admin.site.register(Address)
admin.site.register(Office)
admin.site.register(Devices)
admin.site.register(DevUsers)
