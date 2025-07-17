from django.contrib import admin
from .models import Inventory, RequestForMaterial, RequestForQuotes, QuotationsReceived, PurchasingOrder

admin.site.register(Inventory)
admin.site.register(RequestForMaterial)
admin.site.register(RequestForQuotes)
admin.site.register(QuotationsReceived)
admin.site.register(PurchasingOrder)
