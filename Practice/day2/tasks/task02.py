# TODO: Создайте 4 корутины, каждая из которых возвращает строку.
#  Запустите их параллельно и соберите результаты в список.
import asyncio


async def print_strings(s):
    await asyncio.sleep(2)
    return s


async def main() -> None:
    task_1 = print_strings('Weather')
    task_2 = print_strings('Rain')
    task_3 = print_strings('Sun')
    task_4 = print_strings('Food')

    print('Tasks has been created.')

    result_1 = await task_1
    result_2 = await task_2
    result_3 = await task_3
    result_4 = await task_4

    print(result_1, result_2, result_3, result_4, sep='\n')

asyncio.run(main())
