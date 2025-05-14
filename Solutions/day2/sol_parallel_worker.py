import asyncio
import random
import concurrent

def create_str():
    print('Start create')
    return random.choice(['hello', 'python', 'world', 'golang'])
    
async def main():
    loop = asyncio.get_running_loop()

    # Запуск в настраиваемом пуле процессов:
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
        res1 = loop.run_in_executor(pool, create_str)
        res2 = loop.run_in_executor(pool, create_str)
        res3 = loop.run_in_executor(pool, create_str)
        res4 = loop.run_in_executor(pool, create_str)
        print(await res1)
        print(await res2)
        print(await res3)
        print(await res4)
        

if __name__ == '__main__':
    asyncio.run(main())
