import asyncio


async def my_coroutine(n: int):
    await asyncio.sleep(5) # Имитация долгой операции
    print(f'Корутина {n} завершилась.')
    return f"Результат {n}"


async def main():
    # Создание задач
    task = asyncio.create_task(my_coroutine(1))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), timeout=3)
        print(result)
    except asyncio.TimeoutError:
        print("Задача будет работать больше 3 секунд.")
        result = await task
        print(f'{result = }')


if __name__ == '__main__':
    asyncio.run(main())