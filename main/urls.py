# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='products'),
    path('products_detail/<int:product_id>/', views.products_detail, name='products_detail'),
    path('warehouses/', views.warehouse_list, name='warehouse_list'),
    path('transactions/', views.transaction_list, name='transactions'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('location/', views.location_search, name='location_search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
