import threading
import time

start = time.time()


def task1():
    print("task 1 started")
    for i in range(5):
        print(f"task 1{i}")
    print("task 1 completed")
    
def task2():
    print("task 2 started")
    for i in range(2):
        print(f"task 2: {i}")
    print("task 2 compleated")
    
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end =time.time()

print(f"main thread completed : {round(end-start,2)}")