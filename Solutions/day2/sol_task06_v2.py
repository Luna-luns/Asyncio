# TODO: Напишите асинхронную программу, которая отправляет HTTP-запросы к трём различным веб-сайтам:
#  "https://www.yandex.com", "https://www.google.com" и "https://www.python.org".
#  Как только от одного из сайтов будет получен ответ,
#  необходимо отменить выполнение запросов к остальным сайтам
#  и вывести время, затраченное на получение первого ответа.

import asyncio
import aiohttp
import time

async def fetch_data(session, url):
    response = await session.get(url)
    try:
        print('Answer was taken from '+url)
        return await response.text()
    finally:
        response.close()


async def main(urls):
    session = aiohttp.ClientSession()
    
    try:
        coroutines = [fetch_data(session, url) for url in urls]
        tasks = []
    
        for coroutine in coroutines:
            task = asyncio.create_task(coroutine)
            tasks.append(task)
        
        for result in asyncio.as_completed(tasks):
            await result

            for task in asyncio.tasks.all_tasks():
               print(task)

            for task in tasks:
                task.cancel()
       
    except asyncio.CancelledError:
        print("All other cancelled")

    finally:
        await session.close()

if __name__ == "__main__":
    urls = [
	"https://www.yandex.com",
	"https://www.google.com",
	"https://www.python.org",
    ]

    start_time = time.perf_counter()
    results = asyncio.run(main(urls))
    end_time = time.perf_counter()

    print("Execution_time: "+str(end_time-start_time))