from django.urls import path
from .views import (
    add_inventory, add_request_for_materials,
    add_request_for_quotes, add_quotations_received,
    add_purchasing_order, dashboard
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('add-inventory/', add_inventory, name='add-inventory'),
   
