import json
from threading import Thread, Lock
import time
import urllib
import urllib.request
import string

finished_count = 0

def count_letters(url: str, frequency: dict, lock: Lock) -> None:
    response = urllib.request.urlopen(url)
    text = str(response.read())

    for l in text:
        letter = l.lower()
        if letter not in frequency:
            continue
        with lock:
            frequency[letter] += 1

    global finished_count
    finished_count += 1

def main():
    lock = Lock()
    frequency = {letter: 0 for letter in string.ascii_lowercase}
    start = time.time()
    for i in range(1000, 1050):
        Thread(target=count_letters, args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency, lock)).start()
    end = time.time()

    while finished_count < 50:
        time.sleep(0.1)

    print(json.dumps(frequency, indent=4))
    print("Done, time taken", end - start)

main()