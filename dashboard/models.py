from django.db import models

# 1. Inventory
class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.TextField(blank=True, null=True)
    quantity_in_stock = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name


# 2. Request for Materials
class RequestForMaterials(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity_requested = models.IntegerField()
    requested_by = models.CharField(max_length=100)
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.item.item_name} - {self.status}"


# 3. Request for Quotes
class RequestForQuotes(models.Model):
    STATUS_CHOICES = [
        ('Sent', 'Sent'),
        ('Responded', 'Responded'),
        ('Closed', 'Closed'),
    ]
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    request_date = models.DateField(auto_now_add=True)
    vendor_name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Sent')

    def __str__(self):
        return f"RFQ - {self.vendor_name}"


# 4. Quotations Received
class QuotationsReceived(models.Model):
    rfq = models.ForeignKey(RequestForQuotes, on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=100)
    quoted_price = models.DecimalField(max_digits=10, decimal_places=2)
    quote_date = models.DateField(auto_now_add=True)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return f"Quote from {self.vendor_name}"


# 5. Purchasing Orders
class PurchasingOrders(models.Model):
    STATUS_CHOICES = [
        ('Issued', 'Issued'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    quotation = models.ForeignKey(QuotationsReceived, on_delete=models.CASCADE)
    po_number = models.CharField(max_length=50, unique=True)
    issue_date = models.DateField(auto_now_add=True)
    delivery_date = models.DateField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Issued')

    def __str__(self):
        return self.po_number
