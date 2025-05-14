# TODO: Создайте 4 корутины, каждая из которых возвращает строку.
#  Запустите их и соберите результаты в список.
import asyncio
import random
import time


async def create_str(n):
    await asyncio.sleep(n)
    return random.choice(['hello', 'python', 'world', 'golang'])



async def main():
    task1 = asyncio.create_task(create_str(1))
    task2 = asyncio.create_task(create_str(1))
    task3 = asyncio.create_task(create_str(2))
    task4 = asyncio.create_task(create_str(1))

    res1 = await task1
    res2 = await task2
    res3 = await task3
    res4 = await task4

    print("Result:", [res1, res2, res3 , res4])

if __name__ == '__main__':

    start_time = time.perf_counter()
    results = asyncio.run(main())
    end_time = time.perf_counter()

    print(f"Время выполнения: {end_time - start_time:.2f} секунд")