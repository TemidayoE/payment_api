from django.urls import reverse
from rest_framework.test import APITestCase
from unittest.mock import patch
from rest_framework import status
from unittest import mock

class PaymentTests(APITestCase):
    def setUp(self):
        self.initialize_url = reverse('initialize-payment')  # Set up test URL
        self.valid_email = "test@example.com"
        self.valid_amount = 10000  # Amount in kobo

    @patch('payment_api.utils.initialize_transaction')  # Mock the Paystack call
    def test_initialize_payment_success(self, mock_initialize_transaction):
        """Test initializing payment successfully."""
        # Mock Paystack API response
        mock_initialize_transaction.return_value = {
            "status": True,
            "data": {
                "authorization_url": "https://paystack.com/pay/mock-url",
                "reference": "mock-ref",
            }
        }

        # Make POST request to initialize payment
        response = self.client.post(self.initialize_url, {
            "email": self.valid_email,
            "amount": self.valid_amount
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Assert HTTP 200
        self.assertIn("authorization_url", response.data)  # Assert response contains expected data

    def test_initialize_payment_failure(self):
        # Prepare the payload with invalid data
        payload = {
            # Include the payload without the required 'email' parameter or with an invalid one
            'amount': 1000,
            'currency': 'USD',
            'email': 'invalid_email'  # Simulating invalid email address
        }
        
        # Get the URL for the 'initialize_payment' endpoint
        url = reverse('initialize-payment')  # Assuming 'initialize_payment' is the name of the URL
        
        # Send the POST request with the invalid payload
        response = self.client.post(url, payload, format='json')
        
        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Assert the correct fields and values in the response
        self.assertIn('message', response.data)  # Check for the 'message' field
        self.assertEqual(response.data['message'], 'Invalid Email Address Passed')  # Customize based on your error message
        self.assertIn('meta', response.data)  # Check if 'meta' field is present
        self.assertIn('nextStep', response.data['meta'])  # Ensure 'nextStep' is part of 'meta'
        self.assertEqual(response.data['meta']['nextStep'], "Ensure you're passing the email parameter when creating the charge")  # Customize this
        self.assertEqual(response.data['type'], 'validation_error')  # Check for the error type
        self.assertEqual(response.data['code'], 'invalid_email_address')  # Check for the error code