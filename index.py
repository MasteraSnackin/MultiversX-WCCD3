import requests
import random

# Constants for API endpoints and transaction details
API_URL = "https://devnet-api.multiversx.com"
TOKEN_TRANSFER_AMOUNT = 10000

# Example account and token data (replace with actual data)
issuer_private_key = "issuer_private_key_here"
issuer_address = "issuer_address_here"
token_identifier = "TOKEN-abcdef"

# Function to generate random recipient addresses for testing purposes
def generate_recipient_addresses(num):
    # Note: In a real scenario, use actual recipient addresses
    return [f"erd1{random.randint(10**17, 10**18)}" for _ in range(num)]

# Function to create a transaction object
def create_transaction(sender, receiver, amount, token_id):
    # Create transaction data for ESDT token transfer
    transaction_data = {
        "sender": sender,
        "receiver": receiver,
        "value": "0",  # No EGLD value transfer
        "data": f"ESDTTransfer@{token_id}@{amount:064x}",  # Encoded token transfer data
        "gasLimit": 50000,  # Estimated gas limit
        "chainID": "D"  # Chain ID for Devnet
    }
    return transaction_data

# Function to send a transaction to the blockchain
def send_transaction(transaction):
    try:
        response = requests.post(f"{API_URL}/transactions", json=transaction)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error sending transaction: {e}")
        return None

# Main function to distribute tokens
def main():
    # Generate 1000 random recipient addresses
    recipient_addresses = generate_recipient_addresses(1000)

    # Iterate over each recipient address
    for recipient in recipient_addresses:
        # Create a transaction for each recipient
        transaction = create_transaction(issuer_address, recipient, TOKEN_TRANSFER_AMOUNT, token_identifier)
        # Send the transaction and print the response
        response = send_transaction(transaction)
        if response:
            print(f"Transaction sent to {recipient}: {response}")
        else:
            print(f"Failed to send transaction to {recipient}")

if __name__ == "__main__":
    main()