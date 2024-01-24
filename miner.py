import requests
import hashlib
import json
import random

def mine_crypto(balance):
    # Simulate mining by generating a random hash
    random_number = random.randint(0, 999999)
    data_to_hash = str(random_number)
    hash_result = hashlib.sha256(data_to_hash.encode()).hexdigest()

    # Check if the balance is 1, then add 1 to the balance and reset it to 0
    if balance == 1:
        balance = 0
        print("Mining Successful! New hash:", hash_result)
    else:
        balance += 1

    return balance, hash_result

def send_to_php_server(result):
    # Define the PHP server URL
    php_server_url = 'https://drive.jaduastudios.com/temp/crypto/submit_balance.php'

    # Create a dictionary with the result
    payload = {'result': result}

    # Send a POST request to the PHP server
    response = requests.post(php_server_url, data=payload)

    # Print the server response
    print(response.text)

if __name__ == "__main__":
    # Initial balance
    balance = 0

    # Simulate mining
    balance, mined_result = mine_crypto(balance)

    # Send the result to the PHP server
    send_to_php_server(mined_result)
