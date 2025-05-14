# TODO: Создайте корутину, которая ждет 5 секунд.
#  Запустите ее как задачу и отмените ее через 2 секунды.
import asyncio


async def get_randint():
    await asyncio.sleep(5)


async def main(n: int):
    task = asyncio.create_task(get_randint())
    try:
        await asyncio.wait_for(task, timeout=2)
    except asyncio.exceptions.TimeoutError:
        print("Задача была отменена")


if __name__ == "__main__":
    asyncio.run(main(5))