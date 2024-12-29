import threading
import multiprocessing
import time


def  print_number():
    for i in range(5):
        time.sleep(2)
        print(f"number: {i}")


def print_letters():
    for letter in "abcde":
        print(f"letter: {letter}")

t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()



def square():
    for i in range(9):
        time.sleep(2)
        print(f"square: {i*i}")

def cube():
    for i in range(9):
        time.sleep(3)
        print(f"cube: {i*i*i}")
if __name__=="__main__":
    p1=multiprocessing.Process(target=square)
    p2=multiprocessing.Process(target=cube)

    p1.start()
    p2.start()

    p1.join()
    p2.join()