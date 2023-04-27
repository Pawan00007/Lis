from django.contrib import admin
from .models import Patient, Specimen, LabOrder, Observation, Order

admin.site.register(Patient)
admin.site.register(Specimen)
admin.site.register(LabOrder)
admin.site.register(Observation)
admin.site.register(Order)
