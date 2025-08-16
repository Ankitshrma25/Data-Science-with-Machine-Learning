### Multithreading 
### I/O-bound tasks:Tasks that spend more time waiting for I/O opereations
## Concurrent excution: When you want to improve throuput of your application by performing multiple opereations concurrently

import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")

def print_letter():
    for letter in "abdc":
        time.sleep(2)
        print(f"Letter: {letter}")


## Create 2 threads
t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)



t=time.time()
## start the thread
t1.start()
t2.start()


## wait for the threads to complete
t1.join()
t2.join()
finished_time=time.time()-t
print(finished_time)