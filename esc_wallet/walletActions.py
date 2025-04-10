import requests
from requests.exceptions import RequestException
from rest_framework.exceptions import ValidationError
from esc_transaction.serializer import TokenTransactionCreationSerializer
from decimal import Decimal

def transferFromTreasury(wallet, transaction_type, amount=0,):
    try:
        response = requests.get(f'http://localhost:3000/token/reward/{wallet.public_key}/{amount}')
        response.raise_for_status()  # Raise an error for non-200 responses

        data = response.json()
        
        wallet.balance = wallet.balance + Decimal(amount)
        wallet.save()
        
        transactionData = {
            "transaction_hash": data['tx'],
            "amount": amount,
            "transfered_to": wallet.pk,
            "transaction_type": transaction_type,
            "status": "CONFIRMED"
        }
        
        

        transaction_serializer = TokenTransactionCreationSerializer(data=transactionData)
        if transaction_serializer.is_valid():
            transaction_serializer.save()
            return transaction_serializer.data
        else:
            raise ValidationError(transaction_serializer.errors)

    except RequestException as e:
        print(f"Error during request: {e}")
    except ValueError as e:
        print(f"Data error: {e}")
    except ValidationError as e:
        print(f"Serialization error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
