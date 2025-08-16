### Multithreading with thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number :{number}"

number=[1,2,3,43,5]


with ThreadPoolExecutor(max_workers=4) as excecutor:
    results=excecutor.map(print_number,number)

for result in results:
    print(result)