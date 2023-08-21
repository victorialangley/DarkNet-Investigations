# bitcoin_trace_tool.py

import requests
import json

def trace_bitcoin_transactions(wallet_address):
    try:
        api_url = f"https://api.blockchain.info/rawaddr/{wallet_address}"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            transactions = data.get("txs", [])
            
            if transactions:
                print(f"Transactions associated with wallet address {wallet_address}:")
                for tx in transactions:
                    print(f"Transaction Hash: {tx.get('hash')}")
                    print(f"Amount Received: {sum([out.get('value') for out in tx.get('out')]) / 100000000} BTC")
                    print("-" * 30)
            else:
                print("No transactions found for the given wallet address.")
        else:
            print("Unable to retrieve transaction data.")
    except requests.exceptions.RequestException:
        print("An error occurred while querying the blockchain API.")

if __name__ == "__main__":
    wallet_address = input("Enter the Bitcoin wallet address to trace: ")
    trace_bitcoin_transactions(wallet_address)
