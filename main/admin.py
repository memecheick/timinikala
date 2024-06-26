from django.contrib import admin
from .models import Product, Warehouse, Transaction, Suggestion


admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(Transaction)
admin.site.register(Suggestion)
