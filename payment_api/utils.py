import requests
from django.conf import settings

PAYSTACK_BASE_URL = 'https://api.paystack.co'

def initialize_transaction(name,email,amount):
  headers = {"Authorization" : f'Bearer {settings.PAYSTACK_SECRET_KEY}', "content-Type": 'application.json',} 
  data = {
    'name': name,
    'email': email,
    'amount': amount,
  }
  url = f'{PAYSTACK_BASE_URL}/transaction/initialize'
  response = requests.post(url, json=data,headers = headers)
  return response.json()

def verify_transaction(refrence):
  headers = {"Authorization" : f'Bearer {settings.PAYSTACK_SECRET_KEY}', "content-Type": 'application.json',} 
  url = f'{PAYSTACK_BASE_URL}/transaction/verify/{refrence}'
  response = requests.get(url,headers = headers)
  return response.json()
