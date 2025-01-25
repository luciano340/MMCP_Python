from threading import Thread
import time


def Child():
    print("Doing Child Work...")
    time.sleep(5)
    print("Child work is done...")

def Parent():
    t = Thread(target=Child, args=())
    t.start()
    print("Parent is waiting...")
    t.join()
    print("Parent is not waiting anymore...")

Parent()