import multiprocessing
import os

def hello_from_process():
    print(f'Привет от дочернего процесса {os.getpid()}!')

if __name__ == '__main__':
    hello_first = multiprocessing.Process(target=hello_from_process)
    hello_first.start()
    hello_second = multiprocessing.Process(target=hello_from_process)
    hello_second.start()
    print(f'Привет от родительского процесса {os.getpid()}')
    hello_first.join()
    hello_second.join()