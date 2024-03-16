import requests
import sys
import threading
import time
import asyncio
import aiohttp

async def check_test_status(url):
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    print(response.status)
                    status = await response.json()
                    return status['status']
        except (aiohttp.ClientError, KeyError) as e:
            print("Error checking status:", e)
            return False
        finally:
            await asyncio.sleep(7)  # Adjust delay as needed

def stop_script(signum, frame):
    global running
    running = False
    print("Stopping script...")
# 123r


async def send_request(session, url):
    try:
        async with session.get(url) as response:
            # pass
            print("Request sent to:", url)
            # print("Response:", response.status)
    except aiohttp.ClientError as e:  
        print("Error:", e)

def send_requests_concurrently(url, delay):
    async def worker():
        async with aiohttp.ClientSession() as session:
            while True:
                await send_request(session, url)
                await asyncio.sleep(delay)

    loop = asyncio.new_event_loop()  # Create a loop for this thread
    asyncio.set_event_loop(loop)
    loop.run_until_complete(worker())

# ... (Rest of your code remains the same) ...



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
    flagg = threading.Thread(target=send_requests_concurrently, args=(url, 7))
    flagg.start()
    
    print("Sending HTTP requests concurrently using multithreading...")
    
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=send_requests_concurrently, args=(url, delay))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
