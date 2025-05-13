import asyncio


async def my_coroutine(n: int):
    print(f'Корутина {n} началась.')
    await asyncio.sleep(1) # Имитация долгой операции
    print(f'Корутина {n} завершилась.')
    return f"Результат {n}"


async def main():
    # Создание задач
    task1 = asyncio.create_task(my_coroutine(1))
    task2 = asyncio.create_task(my_coroutine(2))

    print('just one list')
    
    # Ожидание завершения задач и сбор результатов
    result1 = await task1
    result2 = await task2

    print("Результаты:", result1, result2)


if __name__ == '__main__':
    asyncio.run(main())

