from django.contrib import admin
from .models import Doctor, Patient, Nurse, Pharmacist, Laboratory, Accountant, Receptionist, Department

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Nurse)
admin.site.register(Pharmacist)
admin.site.register(Laboratory)
admin.site.register(Accountant)
admin.site.register(Receptionist)
admin.site.register(Department)
