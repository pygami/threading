import threading
import time

def countdown(event, n):
    while n > 0:
        time.sleep(1)
        print(f"Countdown: {n}")
        n -= 1
    event.set()

def celebrate(event):
    event.wait()
    print("Happy New Year!")

event = threading.Event()
t1 = threading.Thread(target=countdown, args=(event, 5))
t2 = threading.Thread(target=celebrate, args=(event,))
t1.start()
t2.start()
t1.join()
t2.join()
