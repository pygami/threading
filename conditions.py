import threading
import time

class SharedQueue:
    def __init__(self):
        self.queue = []
        self.condition = threading.Condition()

    def produce(self, item):
        with self.condition:
            self.queue.append(item)
            self.condition.notify()

    def consume(self):
        with self.condition:
            while not self.queue:
                self.condition.wait()
            return self.queue.pop(0)

def producer_task():
    for i in range(5):
        shared_queue.produce(i)
        time.sleep(1)

def consumer_task():
    for _ in range(5):
        item = shared_queue.consume()
        print("Consumed:", item)
        time.sleep(1)

shared_queue = SharedQueue()
producer_thread = threading.Thread(target=producer_task)
consumer_thread = threading.Thread(target=consumer_task)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
