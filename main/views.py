from django.shortcuts import render, redirect, get_object_or_404
from .forms import SuggestionForm
from .models import Product, Warehouse, Transaction
from django.db.models import Q


def contact(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = SuggestionForm()
    return render(request, 'main/contact.html', {'form': form})


def contact_success(request):
    return render(request, 'main/contact_success.html')


def home(request):
    return render(request, 'main/home.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/products.html', {'products': products})


def products_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'main/products_detail.html', {'product': product})


def warehouse_list(request):
    entrepots = Warehouse.objects.all()
    return render(request, 'main/warehouses.html', {'entrepots': entrepots})


def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'main/transactions.html', {'transactions': transactions})


def location_search(request):
    query = request.GET.get('q', '')
    if query:
        results = Warehouse.objects.filter(
            Q(name__icontains=query) |
            Q(location__icontains=query) |
            Q(manager_name__icontains=query) |
            Q(category__icontains=query)
        )
    else:
        results = Warehouse.objects.none()

    return render(request, 'main/location.html', {'query': query, 'results': results})
