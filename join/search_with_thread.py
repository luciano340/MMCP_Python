

from genericpath import isdir
from os.path import join, isdir
import os
from threading import Lock, Thread
import time


matches = []


def file_search(path: str, filename: str, lock: Lock) -> None:
    print('Searching in:', path)
    child_threads = []

    for file in os.listdir(path):
        full_path = join(path, file)
        if filename in file:
            with lock:
                matches.append(full_path)
        
        if isdir(full_path):
            t = Thread(target=file_search, args=(full_path, filename, lock))
            t.start()
            child_threads.append(t)
    
    for t in child_threads:
        t.join()

def main():
    start = time.time()
    lock = Lock()
    t = Thread(target=file_search, args=("C:\\Users\\Luciano Romão\\projetos", "teste.py", lock))
    t.start()
    t.join()
    for m in matches:
        print("Matched:", m)
    end = time.time()
    print("Done, time taken", end - start)

main()