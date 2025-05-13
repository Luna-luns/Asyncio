# TODO: Создайте 4 корутины, каждая из которых возвращает строку.
#  Запустите их параллельно и соберите результаты в список.
import asyncio

STRINGS: list = ['Weather', 'Rain', 'Sun', 'Food']


async def print_strings(s):
    await asyncio.sleep(10)
    return s

async def main() -> None:
    tasks = [asyncio.create_task(print_strings(STRINGS[i])) for i in range(0, 4)]
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        print(result)

asyncio.run(main())
