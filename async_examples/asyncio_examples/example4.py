import asyncio
import aiohttp


async def fetch_data(session, url):
    """ Асинхронно получает содержимое URL."""
    response = await session.get(url)
    try:
        return await response.json()
    finally:
        response.close()
    

async def main():
    async with aiohttp.ClientSession() as session:
        coroutines = [fetch_data(session, "https://api.kanye.rest") for _ in range(5)]

        results = []
        for coroutine in coroutines:
            task_instance = asyncio.create_task(coroutine)
            results.append(task_instance)

        for result in asyncio.as_completed(results):
            print(await result)


# Запрашиваем 5 цитат с сайта Kanye West
if __name__ == "__main__":
    asyncio.run(main())