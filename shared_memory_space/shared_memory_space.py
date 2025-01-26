import multiprocessing
import time
from multiprocessing.context import Process

def print_array_content(array: list) -> None:
    for _ in range(50):
        print(*array, sep = ", ")
        time.sleep(1)
    

if __name__ == "__main__":
    arr = multiprocessing.Array('i', [-1] * 10, lock=True)
    p = Process(target=print_array_content, args=([arr]))
    p.start()
    for j in range(10):
        time.sleep(2)
        arr[j] += j + 1
    
    print('Modified Array:', *arr)
    p.join()