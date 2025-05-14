# TODO: Напишите асинхронную программу, которая запускает n асинхронных функции. 
#  n - задайте самостоятельно.
#  Каждая функция должна возвращать случайное целое число в диапазоне от 0 до 10
#  и выполняться за случайное время от 1 до 5 секунд
#  После завершения всех функций найдите сумму всех полученных результатов и выведите её на экран.
import asyncio
import random

async def string_returner():
    delay = random.randint(1, 5)
    result = random.randint(0, 10)
    await asyncio.sleep(delay)
    return result


async def main(n : int):
    tasks = [string_returner() for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sum(results)


if __name__ == '__main__':
    print(asyncio.run(main(15)))