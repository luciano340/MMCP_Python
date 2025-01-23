from threading import Thread
import time


def do_something_io_bounce():
    print("Doing something io bounce!")
    time.sleep(1)
    print("Done io bounce!")

def do_something_cpu_bounce():
    print("Doing something cpu bounce!")
    i = 0
    for _ in range(200000):
        i += 1
    print("Done cpu bounce!")

for _ in range(5):
    t = Thread(target=do_something_io_bounce, args=())
    t.start()

for _ in range(5):
    t = Thread(target=do_something_cpu_bounce, args=())
    t.start()