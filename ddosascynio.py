import asyncio
import aiohttp

async def send_request(session, url):
    async with session.get(url) as response:
        print("Request sent to:", url)
        print("Response:", response.status)

async def send_requests_concurrently(url):
    async with aiohttp.ClientSession() as session:
        while True:
            await send_request(session, url)

# ... rest of your setup code ...

async def main():
    #... your setup with url, num_tasks, etc...
    tasks = [send_requests_concurrently(url) for _ in range(num_tasks)]
    await asyncio.gather(*tasks)

asyncio.run(main())