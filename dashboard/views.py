from django.shortcuts import render, redirect
from .forms import (
    InventoryForm, RequestForMaterialsForm,
    RequestForQuotesForm, QuotationsReceivedForm,
    PurchasingOrdersForm
)

def add_inventory(request):
    form = InventoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('add-inventory')
    return render(request, 'add_inventory.html', {'form': form})

def add_request_for_materials(request):
    form = RequestForMaterialsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('add-request-materials')
    return render(request, 'add_request_for_materials.html', {'form': form})

def add_request_for_quotes(request):
    form = RequestForQuotesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('add-request-quotes')
    return render(request, 'add_request_for_quotes.html', {'form': form})

def add_quotations_received(request):
    form = QuotationsReceivedForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('add-quotation')
    return render(request, 'add_quotations_received.html', {'form': form})

def add_purchasing_order(request):
    form = PurchasingOrdersForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('add-purchase-order')
    return render(request, 'add_purchasing_order.html', {'form': form})
