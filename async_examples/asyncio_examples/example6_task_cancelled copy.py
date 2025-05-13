import asyncio


async def my_coroutine(n: int):
    await asyncio.sleep(2) # Имитация долгой операции
    print(f'Корутина {n} завершилась.')
    return f"Результат {n}"


async def main():
    # Создание задач
    task = asyncio.create_task(my_coroutine(1))
    task.cancel()
    print(f"Задача отменена: {task.cancelled()}")
    try:
        await task
    except asyncio.CancelledError:
        print("Задача была отменена")


if __name__ == '__main__':
    asyncio.run(main())