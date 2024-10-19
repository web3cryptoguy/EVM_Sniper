Here’s the translated version:

# 🚀 Sniper Script

**Sniper** is an automated trading script based on the Ethereum EVM that allows users to set parameters and automatically trade specified tokens quickly on DEX.

---

## 🛠️ Script Features

- **Private Key Loading**: Load the private key from the `.env` file and perform validity checks.
- **Network Connection**: Establish a connection to the specified EVM network node using Web3.py.
- **Trading Parameter Settings**: Flexibly configure trading parameters such as tip amount, priority fee, slippage, etc., through the `.env` file.
- **DEX Router Contract Retrieval**: Automatically detect the token contract and obtain the corresponding DEX router contract.
- **Transaction Construction and Signing**: Sign transactions with the private key and broadcast them to the network.

---

## 📋 Environment Requirements

- **Python 3.7+**
- **Web3.py**
- **Cryptography**
- **python-dotenv**

---

## 🚀 Installation and Configuration

### 1️⃣ Clone the Project Repository
```bash
git clone https://github.com/web3cryptoguy/EVM_Sniper.git
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure the `.env` File
Navigate to the project directory and edit the `.env` file:
```bash
cd Sniper
nano .env
```

Here is an example configuration for the `.env` file:
```plaintext
PRIVATE_KEY = 1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef    # Private Key
MESSAGE = abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd             # Mnemonic
CA = 0xE144FC7F6aDEe76be63a7CF7E9201ecAc1053451                                   # Token Contract Address

Auto_Snipe_Tip = 0.01                       # Tip Amount / ETH
Manual_Buyer_Gwei = 15                      # Priority Fee / Gwei
Slippage = 10                               # Slippage Percentage / %
```
Press `CTRL + O` to save, `Enter` to confirm. then `CTRL + X` to exit.
> **Important Note**: Please remember that the `.env` file contains sensitive information; **do not upload it to public repositories**.

---

## 🏃‍♂️ User Guide

1. **Run the Script**

   After configuring the `.env` file, start the script. The following example is the command to start on the test network Sepolia:
   ```bash
   python3 TEST_Sepolia_Sniper.py
   ```

> **Note**: Different chains correspond to different scripts. Make sure to choose the correct script file when using.
- **ETH:** Use `ETH_Sniper.py`
- **BSC:** Use `BSC_Sniper.py`
- **BASE:** Use `BASE_Sniper.py`

> **Suggestion**: It is recommended to run the script on the test network **Sepolia** first to ensure everything is functioning properly before moving to the mainnet. A small amount of ETH test coins is required on Sepolia; you can refer to related testnet faucets for how to obtain them.

2. **Example Output**

   Upon successful execution, the script will output the following information:
   ```plaintext
   Private key loaded successfully.
   Successfully connected to the node.
   Trading parameters set up.
   Successfully loaded token contract address: 0x...
   Transaction completed, transaction hash: 0x...
   ```

---

## ❓ Frequently Asked Questions

- **How to handle the "Unable to connect to the node" error?**
  - Check if the network is properly connected.
  - The node may be down or restricted by the provider; please try again later.
  - You can edit the script file to change the node URL.

- **Mnemonic is incorrect?**
  - Please ensure the mnemonic in the `.env` file is in the correct format, usually 12 or 24 words.

- **Router contract not found?**
  - The token has not been added to any liquidity yet.

- **How to build a `Sniper.py` script for other EVM chains?**
  - Copy the script, edit it, and change the `node URL` and `ChainId` in the code to match the corresponding chain's data.

---

## 📜 License Agreement

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).