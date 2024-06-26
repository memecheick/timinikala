from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    images = models.ImageField(upload_to='main/')
    ingredients = models.TextField()
    instructions = models.TextField()
    prix = models.IntegerField()

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    CATEGORY_CHOICES = [
        ('Entrepôt', 'Entrepôt'),
        ('Supermarché', 'Supermarché'),
        ('Centre commercial', 'Centre commercial'),
    ]

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    manager_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    location_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    objects = None
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transaction_type = models.CharField(max_length=10, choices=[('IN', 'Entry'), ('OUT', 'Exit')])
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - {self.transaction_type}"


class Suggestion(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Suggestion de {self.name}"
