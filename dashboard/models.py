# Example for Inventory model
class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.TextField(blank=True)
    quantity_in_stock = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)
