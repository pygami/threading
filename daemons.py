import threading
import time

def daemon_thread_function():
    while True:
        print("Daemon thread is running...")
        time.sleep(1)

daemon_thread = threading.Thread(target=daemon_thread_function)
daemon_thread.daemon = True
daemon_thread.start()
time.sleep(3)  # Let main thread sleep to observe daemon thread output
