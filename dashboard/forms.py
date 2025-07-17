from django import forms
from .models import Inventory, RequestForMaterials, RequestForQuotes, QuotationsReceived, PurchasingOrders

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['item_name', 'item_description', 'quantity_in_stock', 'unit_price']

class RequestForMaterialsForm(forms.ModelForm):
    class Meta:
        model = RequestForMaterials
        fields = ['item', 'quantity_requested', 'requested_by', 'status']

class RequestForQuotesForm(forms.ModelForm):
    class Meta:
        model = RequestForQuotes
        fields = ['item', 'quantity', 'vendor_name', 'status']

class QuotationsReceivedForm(forms.ModelForm):
    class Meta:
        model = QuotationsReceived
        fields = ['rfq', 'vendor_name', 'quoted_price', 'selected']

class PurchasingOrdersForm(forms.ModelForm):
    class Meta:
        model = PurchasingOrders
        fields = ['quotation', 'po_number', 'delivery_date', 'total_amount', 'status']
