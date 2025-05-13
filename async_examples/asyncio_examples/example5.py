import asyncio
import aiohttp
import time

async def fetch_data(session, url):
    """ Асинхронно получает содержимое URL."""
    response = await session.get(url)
    try:
        return await response.text()
    finally:
        response.close()
    

async def main(urls):
    session = aiohttp.ClientSession()
    try: 
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks) # coro -> task
        return results
    finally:
        await session.close()


if __name__ == "__main__":
    urls = [
        "https://www.python.org",
        "https://github.com",
        "https://yandex.ru",
        "https://rutube.ru"
    ]

    start_time = time.perf_counter()
    results = asyncio.run(main(urls))
    end_time = time.perf_counter()

    for result in results:
        print(f"Получено {len(result)} байт.")

    print(f"Время выполнения: {end_time - start_time:.2f} секунд")