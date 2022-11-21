import threading
import time

class ThreadPool:
    def __init__(self, max_workers):
        self.max_workers = max_workers
        self.semaphore = threading.Semaphore(max_workers)

    def execute_task(self, task):
        with self.semaphore:
            task()

def worker_task():
    time.sleep(1)
    print("Task completed")

thread_pool = ThreadPool(max_workers=3)
tasks = [worker_task for _ in range(10)]
for task in tasks:
    thread_pool.execute_task(task)
