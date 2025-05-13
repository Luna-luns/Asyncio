import asyncio


async def my_coroutine(n: int):
    await asyncio.sleep(10) # Имитация долгой операции
    print(f'Корутина {n} завершилась.')
    return f"Результат {n}"


async def main():
    # Создание задач
    long_task = asyncio.create_task(my_coroutine(1))
    seconds_elapsed = 0

    while not long_task.done():
        print("Task not finished, checking again in a second.")
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed == 5:
            long_task.cancel()

    try:
        await long_task
    except asyncio.CancelledError:
        print("Задача была отменена")


if __name__ == '__main__':
    asyncio.run(main())