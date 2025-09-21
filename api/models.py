from django.db import models
import uuid

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255) # [cite: 76]
    code = models.CharField(max_length=100, unique=True) # [cite: 76]
    phone_number = models.CharField(max_length=20) # Needed for SMS
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    item = models.CharField(max_length=255) # [cite: 77]
    amount = models.DecimalField(max_digits=10, decimal_places=2) # [cite: 77]
    time = models.DateTimeField(auto_now_add=True) # [cite: 77]

    def __str__(self):
        return f"Order for {self.item} by {self.customer.name}"