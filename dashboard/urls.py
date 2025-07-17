from django.urls import path
f
from .views import (
    add_inventory, add_request_for_materials,
    add_request_for_quotes, add_quotations_received,
    add_purchasing_order, dashboard
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('add-inventory/', add_inventory, name='add-inventory'),
    path('add-request-materials/', add_request_for_materials, name='add-request-materials'),
    path('add-request-quotes/', add_request_for_quotes, name='add-request-quotes'),
    path('add-quotation/', add_quotations_received, name='add-quotation'),
    path('add-purchase-order/', add_purchasing_order, name='add-purchase-order'),
]