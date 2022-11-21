import threading
import time


def task1():
    print("Task 1 started")
    time.sleep(2)  
    print("Task 1 completed")


def task2():
    print("Task 2 started")
    time.sleep(3)  
    print("Task 2 completed")

if __name__ == "__main__":
    
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)
    
    
    thread1.start()
    thread2.start()
    
    
    thread1.join()
    thread2.join()
    
    print("All tasks completed")
