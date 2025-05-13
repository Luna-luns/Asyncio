# TODO: Создайте корутину, которая ждет 5 секунд.
#  Запустите ее как задачу и отмените ее через 2 секунды.

import asyncio


async def waiting_coro() -> None:
    await asyncio.sleep(5)
    print('Evening')


async def get_result() -> None:
    task = asyncio.create_task(waiting_coro())
    task.cancel()
    print('Oops.')
    try:
        await task
    except asyncio.CancelledError:
        print("C'est la vie.")

asyncio.run(get_result())
