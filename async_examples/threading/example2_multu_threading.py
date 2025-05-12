import threading

def hello_from_thread():
    print(f'Привет от потока {threading.current_thread()}!')

hello_first = threading.Thread(target=hello_from_thread)
hello_first.start()
hello_second = threading.Thread(target=hello_from_thread)
hello_second.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name
print(f'В данный момент Python выполняет {total_threads} потокa')
print(f'Имя текущего потока {thread_name}')
hello_first.join()
hello_second.join()