import asyncio
import random


async def my_coroutine(n: int):
    print(f'Корутина {n} началась.')
    delay = random.uniform(1, 4)
    await asyncio.sleep(delay) # Имитация долгой операции
    print(f'Корутина {n} завершилась.')
    return f"Результат {n} за {delay:.2f} секунд."


async def main():
    """ Пример использования asyncio.as_completed()."""
    # Создание задач
    tasks = [asyncio.create_task(my_coroutine(i)) for i in range(1, 4)]
    
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        print('Получен результат:', result)


if __name__ == '__main__':
    asyncio.run(main())

