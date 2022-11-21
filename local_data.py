import threading

thread_local_data = threading.local()

def set_thread_local_value(value):
    thread_local_data.value = value

def get_thread_local_value():
    return getattr(thread_local_data, 'value', None)

set_thread_local_value(42)

def print_thread_local_value():
    print("Thread local value:", get_thread_local_value())

t1 = threading.Thread(target=print_thread_local_value)
t1.start()
t1.join()
