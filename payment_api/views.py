from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from payment_api.utils import  initialize_transaction, verify_transaction
from payment_api.models import Transaction  

class InitializePaymentView(APIView):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        amount = request.data.get('amount')
       
        response = initialize_transaction(name, email, amount)
        if response.get('status'):
            transaction = Transaction.objects.create(
                name=name,
                email=email,
                amount=amount,
                reference=response['data']['reference']
            )
            return Response(response['data'], status=status.HTTP_200_OK)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
      
class VerifyPaymentView(APIView):
    def get(self, request, reference):
      
        response = verify_transaction(reference)
        if response.get('status'):
            transaction = Transaction.objects.get(reference=reference)
            transaction.status = 'success' if response['data']['status'] == 'success' else 'failed'
            transaction.save()
            return Response(response['data'], status=status.HTTP_200_OK)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)