from django.urls import path
from . import views
from .views import (
    add_inventory, add_request_for_materials,
    add_request_for_quotes, add_quotations_received,
    add_purchasing_order, dashboard, inventory_list
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('inventory/', inventory_list, name='inventory-list'),
    path('add-inventory/', add_inventory, name='add-inventory'),
    path('add-request-materials/', add_request_for_materials, name='add-request-materials'),
    path('add-request-quotes/', add_request_for_quotes, name='add-request-quotes'),
    path('add-quotation/', add_quotations_received, name='add-quotation'),
    path('add-purchase-order/', add_purchasing_order, name='add-purchase-order'),
]