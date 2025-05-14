import asyncio
from tools import async_timed, delay


@async_timed()
async def main() -> None:
    delay_times = (3, 3, 3)
    [await asyncio.create_task(delay(seconds)) for seconds in delay_times]


@async_timed()
async def main2() -> None:
    delay_times = (3, 3, 3)
    tasks = [asyncio.create_task(delay(seconds)) for seconds in delay_times]
    [await task for task in tasks]


if __name__ == '__main__':
    asyncio.run(main2())
