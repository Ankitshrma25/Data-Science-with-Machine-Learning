## Process that run in parallel
### CPU bound Tasks: Task that are heavy on CPU usage (eg. Mathematical Computation)
## Parallel Excution- Multiple cores of the CPU

import multiprocessing

import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square is: {i*i}")
    
def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")


## Entery point

if __name__=="__main__":

    ## Calling the function

    ## create two processes
    p1=multiprocessing.Process(target=square_numbers)
    p2=multiprocessing.Process(target=cube_numbers)


    t=time.time()

    ## Start the Process
    p1.start()
    p2.start()

    ## Wait for the process to complete
    p1.join()
    p2.join()


    finished_time=time.time()-t
    print(finished_time)