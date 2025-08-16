## Multi processing with ProcessPoolExcutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(2)
    return f"Square: {number*number}"

numbers=[1,2,3,4,5,6,2,3,0,1,2,3,4,5,6,12,11,10]

## Entry Point
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(square_number,numbers)

    for result in results:
        print(result)