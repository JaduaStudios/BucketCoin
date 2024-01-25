import requests
import hashlib
import json
import random
import concurrent.futures

def calculate_hash(data_to_hash):
    return hashlib.sha256(data_to_hash.encode()).hexdigest()

def mine_crypto(username, password, balance, num_processes=61):
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        # Increase CPU usage by parallelizing hash calculations
        random_numbers = [random.randint(0, 999999) for _ in range(100000)]
        data_to_hashes = [str(random_number) for random_number in random_numbers]

        hash_results = list(executor.map(calculate_hash, data_to_hashes))

    # Use the last hash result as the final result
    hash_result = hash_results[-1]

    balance += 1
    print("Mining Successful! New hash:", hash_result)

    return balance, hash_result, username, password


def send_to_php_server(result, username, password):
    # Define the PHP server URL
    php_server_url = 'https://drive.jaduastudios.com/temp/crypto/submit_balance.php'

    # Create a dictionary with the result, username, and password
    payload = {'result': result, 'username': username, 'password': password}

    # Send a POST request to the PHP server
    response = requests.post(php_server_url, data=payload)

    # Print the server response
    print(response.text)

if __name__ == "__main__":
    # Initial balance
    balance = 0

    # Replace with values from JSON
    username = 'test'
    password = 'test'

    # Number of coins to mine (get from JSON)
    num_iterations = 10

    for _ in range(num_iterations):
        # Simulate mining
        balance, mined_result, username, password = mine_crypto(username, password, balance)
        
        # Send the hash to the PHP server
        send_to_php_server(mined_result, username, password)
