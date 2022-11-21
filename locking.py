import threading

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1

counter = Counter()
threads = [threading.Thread(target=counter.increment) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("Counter value with Lock:", counter.value)
