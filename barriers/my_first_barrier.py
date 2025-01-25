import datetime
from threading import Barrier, Thread
import time


barrier = Barrier(2)

def wait_on_barrier(name: str, time_sleep: int) -> None:
    for i in range(10):
        print(name, "running")
        time.sleep(time_sleep)
        print(name, f'is waiting on barrier {datetime.datetime.now()}')
        barrier.wait()
    
    print(name, "Is Finished!")

red = Thread(target=wait_on_barrier, args=["red", 4])
blue = Thread(target=wait_on_barrier, args=["blue", 10])
red.start()
blue.start()
time.sleep(8)
print("Aborting barrier")
barrier.abort()