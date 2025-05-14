# TODO: Напишите асинхронную программу, которая запускает n асинхронных функции. 
#  n - задайте самостоятельно.
#  Каждая функция должна возвращать случайное целое число в диапазоне от 0 до 10
#  и выполняться за случайное время от 1 до 5 секунд
#  После завершения всех функций найдите сумму всех полученных результатов и выведите её на экран.

import asyncio
import random


async def get_randint():
    delay = random.randint(1, 5)
    number = random.randint(0, 10)
    await asyncio.sleep(delay)
    return number


async def main(n: int):
    tasks = [asyncio.create_task(get_randint()) for _ in range(n)]
    num_list = []

    for compiled in asyncio.as_completed(tasks):
        result = await compiled
        print(result)
        num_list.append(result)
    print(sum(num_list))


if __name__ == "__main__":
    asyncio.run(main(5))