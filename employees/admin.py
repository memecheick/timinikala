# employees/admin.py

from django.contrib import admin
from .models import Department, Employee, Leave, Absence, PaymentConfirmation

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Leave)
admin.site.register(Absence)
admin.site.register(PaymentConfirmation)
