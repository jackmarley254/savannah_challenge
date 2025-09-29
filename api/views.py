# handle the HTTP requests and connect models to serializers.

from rest_framework import viewsets, permissions
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from .services import send_order_alert_sms
from django.http import JsonResponse

def status_view(request):
         """Returns a simple JSON response to confirm the API is up."""
         return JsonResponse({"status": "ok", "message": "Savannah API is running"})


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # Allow any authenticated user to view customers, but maybe only admins to create?
    permission_classes = [permissions.IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet): 
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Save the order instance first
        order = serializer.save()
        
        # Get customer details
        customer = order.customer
        
        # Format the message
        message = f"Dear {customer.name}, your order for {order.item} amounting to {order.amount} has been received."
        
        # Send the SMS 
        send_order_alert_sms(customer.phone_number, message)