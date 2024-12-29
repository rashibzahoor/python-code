from concurrent.futures import ProcessPoolExecutor
import time


def square_numbers(number):
    time.sleep(4)
    return f"number: {number*number}"

numbers=[2,3,4,5,6,7,8,9]
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=2) as executor:
        results=executor.map(square_numbers,numbers)
    for result in results:
     print(result)