# TODO: Напишите асинхронную программу, которая отправляет HTTP-запросы к трём различным веб-сайтам:
#  "https://www.yandex.com", "https://www.google.com" и "https://www.python.org".
#  Как только от одного из сайтов будет получен ответ,
#  необходимо отменить выполнение запросов к остальным сайтам
#  и вывести время, затраченное на получение первого ответа.

import asyncio
import aiohttp
import certifi
import ssl
import time


async def fetch_data(session, url, ssl):
    response = await session.get(url, ssl=ssl)
    sync_start = time.perf_counter()
    try:
        await response.text()
        sync_end = time.perf_counter()
        return sync_end - sync_start
    finally:
        response.close()


async def main():
    addresses = ["https://www.yandex.com", "https://www.google.com","https://www.python.org"]
    async with aiohttp.ClientSession() as session:
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        coroutines = [asyncio.create_task(fetch_data(session, address, ssl=ssl_context)) for address in addresses]

        done, pending = await asyncio.wait(
            coroutines, return_when=asyncio.FIRST_COMPLETED
        )

        result = await list(done)[0]
        print("Первый результат:", result)


        for t in pending:
            t.cancel()


if __name__ == '__main__':
    asyncio.run(main())