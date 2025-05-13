# TODO: Создайте несколько асинхронных задач с разными задержками.
#  Используйте asyncio.as_completed() для обработки результатов задач по мере их завершения.
#  Выведите результаты каждой задачи сразу после ее завершения.

import asyncio
import random


async def some_task() -> str:
    delay = random.uniform(2, 7)
    await asyncio.sleep(delay)
    return f'Courutine was over in {delay:.2f} seconds.'


async def get_result() -> None:
    tasks = [asyncio.create_task(some_task()) for _ in range(1, 6)]
    results = [await task for task in asyncio.as_completed(tasks)]
    print('\n'.join(results))


asyncio.run(get_result())
