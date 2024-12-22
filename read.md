# Token Distribution Script

This project provides a Python script to distribute fungible tokens on the MultiversX blockchain's Devnet. The script generates transactions to transfer tokens from an issuer's account to multiple recipient accounts.

## Prerequisites

- Python 3.x installed on your system.
- Access to the MultiversX Devnet for testing.
- `requests` library for Python (install via pip if not already installed).

## Installation

1. Clone the repository or download the script file.
2. Install necessary Python packages:
   ```bash
   pip install requests
Configuration
Before running the script, you need to configure it with your account and token details.

Open the script file (token_distribution.py).
Replace the following placeholders with actual data:
issuer_private_key: Your private key for the issuer account. (Note: Handle securely)
issuer_address: Your issuer account address.
token_identifier: The identifier for the token you wish to distribute.
Usage
To execute the script, run the following command in your terminal:

bash
Copy
python token_distribution.py
How It Works
The script generates 1,000 random recipient addresses.
It creates and sends a transaction for each recipient, transferring a specified amount of tokens.
The transaction data encodes the ESDT transfer operation using the token identifier.
Each transaction is sent to the MultiversX Devnet via the API.
Verification
After executing the script, you can verify the transactions and token distribution using the MultiversX Devnet Explorer:

Go to MultiversX Devnet Explorer.
Search for your token identifier to check the number of holders and transaction details.
Important Considerations
Security: Ensure the private key is securely stored and not exposed in your code.
Testing: This script is intended for testing purposes on the Devnet. Avoid using it on the mainnet without thorough validation.
Real Addresses: Replace randomly generated addresses with actual recipient addresses in a production scenario.
Documentation
For more detailed information on interacting with the MultiversX blockchain, refer to the following resources:

MultiversX Fungible Tokens Documentation
MultiversX Python SDK Cookbook
MultiversX REST API Documentation
License
This project is licensed under the MIT License. See the LICENSE file for more information.

Copy

### Key Points in the README:

- **Overview**: A brief description of what the script does.
- **Prerequisites**: Required software and libraries.
- **Installation**: Steps to set up the environment.
- **Configuration**: Instructions to replace placeholder data with actual account details.
- **Usage**: How to run the script.
- **Verification**: How to verify the results using the Devnet Explorer.
- **Important Considerations**: Highlights on security and testing.
- **Documentation**: Links to further resources for understanding the MultiversX blockchain.
- **License**: Placeholder for licensing information.

Make sure to adjust the README as necessary to fit any additional details specific to your implementation or organizational requirements.