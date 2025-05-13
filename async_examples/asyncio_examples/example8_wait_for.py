import asyncio


async def my_coroutine(n: int):
    await asyncio.sleep(10) # Имитация долгой операции
    print(f'Корутина {n} завершилась.')
    return f"Результат {n}"


async def main():
    # Создание задач
    task = asyncio.create_task(my_coroutine(1))

    try:
        result = await asyncio.wait_for(task, timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("Задача была отменена?")
        print("Check:", task.cancelled())


if __name__ == '__main__':
    asyncio.run(main())