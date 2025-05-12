# Синхронное чтение кода состояния

import time
import requests
import threading


def read_example() -> None:
    response = requests.get('https://example.com')
    print('Status code:', response.status_code)


thread1 = threading.Thread(target=read_example)
thread2 = threading.Thread(target=read_example)

sync_start = time.perf_counter()
thread1.start()
thread2.start()
print("Все потоки работают")
thread1.join()
thread2.join()
sync_end = time.perf_counter()

print(f"Выполнение кода заняло: {sync_end - sync_start:.4f} с.")
