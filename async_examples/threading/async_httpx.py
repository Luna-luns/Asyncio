# Синхронное чтение кода состояния

import asyncio
import time
import httpx


urls = ('https://example.com', 'https://youtube.com', 'https://vk.com')

def sync_call() -> None:
    for i in range(len(urls)):
        print("Get sync response from url:", urls[i])
        response = httpx.get(urls[i])
        print('Status code:', response.status_code)


async def async_call(url):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        print("Get async response from url:", url)
        print(r.status_code)


async def async_call_all(local_urls):
    """ Make tasks from <async_call>"""
    return await asyncio.gather(*[async_call(url) for url in local_urls])


print("Running sync ...")
sync_start = time.perf_counter()
sync_call() # операция блокирующая
sync_end = time.perf_counter()

print(f"Выполнение кода заняло: {sync_end - sync_start:.4f} с.")

print("Running async ...")
async_start = time.perf_counter()
asyncio.run(async_call_all(urls))
async_end = time.perf_counter()

print(f"Выполнение кода заняло: {async_end - async_start:.4f} с.")