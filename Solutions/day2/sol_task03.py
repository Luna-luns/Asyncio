# TODO: Создайте несколько асинхронных задач с разными задержками.
#  Используйте asyncio.as_completed() для обработки результатов задач по мере их завершения.
#  Выведите результаты каждой задачи сразу после ее завершения.
import asyncio
import random

async def wait_random(i : int):
    delay = random.randint(1, 5)
    await asyncio.sleep(delay)
    return f"Номер задачи {i + 1}. Задача завершилась через {delay} секунд"

async def main():
    tasks = [asyncio.create_task(wait_random(i)) for i in range(3)]
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)

if __name__ == '__main__':
    asyncio.run(main())