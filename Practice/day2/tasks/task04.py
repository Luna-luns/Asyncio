# TODO: Напишите асинхронную программу, которая запускает n асинхронных функции. n - задайте самостоятельно
#  Каждая функция должна возвращать случайное целое число в диапазоне от 0 до 10
#  и выполняться за случайное время от 1 до 5 секунд
#  После завершения всех функций найдите сумму всех полученных результатов и выведите её на экран.

import asyncio
import random


async def get_random_num() -> int:
    num = random.randint(0, 10)
    delay = random.randint(1, 4)
    await asyncio.sleep(delay)
    print(num)
    return num


async def get_sum() -> None:
    results: tuple = await asyncio.gather(get_random_num(), get_random_num(), get_random_num())
    print(f'Total sum = {sum(results)}')


asyncio.run(get_sum())
