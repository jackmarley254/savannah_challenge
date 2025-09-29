from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from unittest.mock import patch
from .models import Customer

class ApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # "Log in" the test user for authenticated requests
        self.client.force_authenticate(user=self.user)
        # Create a test customer
        self.customer = Customer.objects.create(
            name='jack',
            code='CUST001',
            phone_number='+254797404295'
        )

    def test_create_customer(self):
        """
        Test that we can create a customer.
        """
        url = '/api/customers/'
        data = {'name': 'jack', 'code': 'CUST002', 'phone_number': '+254755895615'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Customer.objects.count(), 2)

    @patch('api.views.send_order_alert_sms')
    def test_create_order_sends_sms(self, mock_send_sms):
        """
        Test that creating an order triggers the SMS service. 
        """
        url = '/api/orders/'
        data = {
            'customer': str(self.customer.id),
            'item': 'Test Item',
            'amount': '99.99'
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, 201)
        # Check that our mock function was called exactly once
        mock_send_sms.assert_called_once()