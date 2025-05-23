# TODO: дана асинхронная функция которая ждет случайное количество секунд (от 1 до 5)
#  Создайте 3 корутины, и запустите их асинхронно с помощью asyncio.gather().

import asyncio
import random


async def wait_random() -> None:
    delay = random.randint(1, 5)
    await asyncio.sleep(delay)
    print(f"Задача завершилась через {delay} секунд")


async def main() -> None:
    await asyncio.gather(wait_random(), wait_random(), wait_random())


if __name__ == '__main__':
    asyncio.run(main())
