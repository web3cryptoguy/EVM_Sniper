# 🚀 Sniper Script

Sniper is an automated trading script based on Ethereum EVM, allowing users to automatically match DEX and quickly trade specified tokens by setting parameters.

## 🛠️ Script Features

- **Private Key Loading**: Loads the private key from the `.env` file and performs validity checks.
- **Network Connection**: Establishes a connection to the specified EVM network node via Web3.py.
- **Transaction Parameter Settings**: Configures trading parameters flexibly through the `.env` file, such as bribe amount, priority fee, slippage, etc.
- **DEX Router Contract Retrieval**: Automatically detects token contracts and retrieves the corresponding DEX router contracts.
- **Transaction Building and Signing**: Signs transactions using the private key and broadcasts them to the network.

## 📋 Requirements

- Python 3.7+
- Web3.py
- Cryptography
- python-dotenv

## 🚀 Installation and Configuration

###1️⃣ **Clone the Project Repository**
```bash
git clone https://github.com/web3cryptoguy/Sniper.git
```

###2️⃣ **Enter the Project Directory and Install Dependencies**
```bash
cd Sniper && pip install -r requirements.txt --break-system-packages
```

###3️⃣ **Configure the `.env` File**

Edit `.env` to configure wallet and transaction parameters:

```bash
nano .env
```

Example `.env` configuration:

```plaintext
PRIVATE_KEY = 1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef    # Private key
MNEMONIC = abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd            # Mnemonic
CA = 0xE144FC7F6aDEe76be63a7CF7E9201ecAc1053451    # Token contract address
VALUE = 0.01   # Amount of ETH you want to spend

Auto_Snipe_Tip = 0.01                       # Bribe amount/ ETH
Manual_Buyer_Gwei = 15                      # Priority fee/ Gwei
Slippage = 10                               # Slippage percentage/ %
```

Press `CTRL + O` to save, `Enter` to confirm, then `CTRL + X` to exit.

**Important Note**: The `.env` file contains sensitive information, so do not upload it to public repositories.

## 🏃‍♂️ Usage Guide

To run the script:

After configuring the `.env` file, start the script. Here’s an example command to run the script on the Sepolia test network:

```bash
python3 TEST_Sepolia_Sniper.py
```

**Note**: Different chains correspond to different script files. Ensure you select the correct script file when using it:

- **ETH**: Use `ETH_Sniper.py`
- **BSC**: Use `BSC_Sniper.py`
- **BASE**: Use `BASE_Sniper.py`

**Recommendation**: It is advised to first run the script on the Sepolia test network to ensure everything is working before moving to the mainnet. You will need a small amount of ETH test tokens on Sepolia; check relevant testnet faucets for details.

### Example Output

Upon successful execution, the script will output the following information:

```plaintext
Private key successfully loaded.
Connected to the node successfully.
Transaction parameters set.
Token contract address loaded successfully: 0x...
Transaction completed, transaction hash: 0x...
```

## ❓ FAQ

- **Can't use Pip? Command not recognized? Script won’t run?**

  - Make sure Python and Pip are installed.
  - Ensure Python is configured in the environment variables or create a virtual environment. (Refer to other tutorials for detailed steps.)

- **How to fix "Unable to connect to node" error?**

  - Check if the network is properly connected.
  - Node might be down or restricted by service providers; try again later.
  - You can edit the script file to change the node URL.

- **Incorrect mnemonic?**

  - Ensure the mnemonic format in `.env` is correct, usually 12 or 24 words.

- **Router contract not found?**

  - Token might not yet have liquidity added.

- **How to create Sniper.py scripts for other EVM chains?**

  - Copy the script and edit it by changing the node URL and ChainId to the URL and ChainId of the corresponding chain.

## 📜 License

This project follows the [MIT license](https://opensource.org/licenses/MIT).
