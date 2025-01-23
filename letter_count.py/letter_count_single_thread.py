import json
import time
import urllib
import urllib.request
import string

def count_letters(url: str, frequency: dict ) -> None:
    response = urllib.request.urlopen(url)
    text = str(response.read())

    for l in text:
        letter = l.lower()
        if letter not in frequency:
            continue
        frequency[letter] += 1

def main():
    frequency = {letter: 0 for letter in string.ascii_lowercase}
    start = time.time()
    for i in range(1000, 1050):
        count_letters(url=f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency=frequency)
    
    end = time.time()
    print(json.dumps(frequency))
    print("Done, time taken", end - start)

main()