

from genericpath import isdir
from os.path import join, isdir
import os
from threading import Lock, Thread
import time

from wait_group import WaitGroup


matches = []


def file_search(path: str, filename: str, lock: Lock, wait_group: WaitGroup) -> None:
    print('Searching in:', path)

    for file in os.listdir(path):
        full_path = join(path, file)
        if filename in file:
            with lock:
                matches.append(full_path)
        
        if isdir(full_path):
            wait_group.add(1)
            t = Thread(target=file_search, args=(full_path, filename, lock, wait_group))
            t.start()
            wait_group.done()
    wait_group.done()

def main():
    start = time.time()
    wait_group = WaitGroup()
    wait_group.add(1)
    lock = Lock()
    t = Thread(target=file_search, args=("C:\\Users\\Luciano Romão\\projetos", "teste.py", lock, wait_group))
    t.start()
    wait_group.wait()
    for m in matches:
        print("Matched:", m)
    end = time.time()
    print("Done, time taken", end - start)

main()