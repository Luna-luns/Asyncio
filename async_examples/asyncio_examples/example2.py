import asyncio
import random


async def my_coroutine(n: int):
    print(f'Корутина {n} началась.')
    delay = random.uniform(1, 4)
    await asyncio.sleep(delay) # Имитация долгой операции
    print(f'Корутина {n} завершилась.')
    return f"Результат {n} за {delay:.2f} секунд."


async def main():
    # Создание задач
    # task1 = asyncio.create_task(my_coroutine(1))
    task2 = asyncio.create_task(my_coroutine(2))
    task3 = asyncio.create_task(my_coroutine(3))
    
    # Ожидание завершения задач и сбор результатов
    # results = await asyncio.gather(task1, task2, task3)
    results = await asyncio.gather(my_coroutine(1), task2, task3)

    print("Результаты:", results)

# Корутины работают сейчас асинхронно, но результаты будут получены только тогда,
# когда отработают все горутины.
if __name__ == '__main__':
    asyncio.run(main())

