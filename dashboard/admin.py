from django.contrib import admin
from .models import Inventory, RequestForMaterials, RequestForQuotes, QuotationsReceived, PurchasingOrders

admin.site.site_header = 'Purchase Management System Dashboard'


admin.site.register(Inventory)    
admin.site.register(RequestForMaterials)
admin.site.register(RequestForQuotes)
admin.site.register(QuotationsReceived)
admin.site.register(PurchasingOrders)
