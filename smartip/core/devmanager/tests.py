from django.test import TestCase


# Create your tests here.
from core.devmanager.models import DevType

query = DevType.objects.all()
print(query)