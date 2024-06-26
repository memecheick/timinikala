# employees/models.py

from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name}"


class Absence(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name}"


class PaymentConfirmation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    payment_date = models.DateField("Date de Paiement")
    is_paid = models.BooleanField("Paiement effectué", default=False)
    confirmation_date = models.DateField("Date de Confirmation", null=True, blank=True)

    class Meta:
        verbose_name = "Confirmation de Paiement"
        verbose_name_plural = "Confirmations de Paiement"

    def __str__(self):
        return f"Confirmation de paiement pour {self.employee.first_name} {self.employee.last_name}"
