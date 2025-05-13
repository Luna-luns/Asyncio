# TODO: Напишите асинхронную программу, которая отправляет HTTP-запросы к трём различным веб-сайтам:
#  "https://www.yandex.com", "https://www.google.com" и "https://www.python.org".
#  Как только от одного из сайтов будет получен ответ,
#  необходимо отменить выполнение запросов к остальным сайтам
#  и вывести время, затраченное на получение первого ответа.

import asyncio
import time
from aiohttp import ClientSession

URLS: list = ["https://www.python.org", "https://github.com", "https://yandex.ru", "https://rutube.ru"]


async def get_web_data(session: ClientSession, url: str) -> None:
    result = await session.get(url=url, ssl=False)
    result.raise_for_status()
    await result.text()


async def get_result() -> None:
    start_time = time.perf_counter()
    async with ClientSession() as session:
        tasks = [asyncio.create_task(get_web_data(session, url)) for url in URLS]
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

        first_result_time = time.perf_counter() - start_time

        print(f"Первый ответ получен за {first_result_time:.2f} секунд")

        for task in pending:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                ...
        print("Все остальные запросы отменены.")


asyncio.run(get_result())
