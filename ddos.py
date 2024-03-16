import requests
import sys
import threading
import time

def send_request(url):
    try:
        response = requests.get(url)
        print("Request sent to:", url)
        print("Response:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

def send_requests_concurrently(url, delay):
    while True:
        send_request(url)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <IP> <port>")
        sys.exit(1)
    
    ip = sys.argv[1]
    port = sys.argv[2]
    # url = f"http://{ip}:{port}"  # Combine IP and port to form the URL

    url = f"http://{ip}"  # Combine IP and port to form the URL
    delay = 0  # Adjust the delay (in seconds) between each request
    num_threads = 500  # Number of concurrent threads
    
    print("Sending HTTP requests concurrently using multithreading...")
    
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=send_requests_concurrently, args=(url, delay))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
