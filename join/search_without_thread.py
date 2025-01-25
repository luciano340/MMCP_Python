

from genericpath import isdir
from os.path import join, isdir
import os
import time


matches = []


def file_search(path: str, filename: str) -> None:
    print('Searching in:', path)
    
    for file in os.listdir(path):
        full_path = join(path, file)
        if filename in file:
            matches.append(full_path)
        
        if isdir(full_path):
            file_search(full_path, filename)

def main():
    start = time.time()
    file_search(path="C:\\Users\\Luciano Romão\\projetos", filename="teste.py")
    for m in matches:
        print("Matched:", m)
    end = time.time()
    print("Done, time taken", end - start)

main()