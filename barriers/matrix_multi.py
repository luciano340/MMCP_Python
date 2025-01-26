from threading import Barrier, Thread, Lock
import time
from random import choice, randint

matrix_size = 200
stop_threads = False
barrier_start = Barrier(matrix_size + 1)
barrier_done = Barrier(matrix_size + 1)
start = time.time()
results = [[0] * matrix_size for r in range(matrix_size)]

def matrix_factory() -> list:
    return [choice([randint(-100, -1), randint(1, 100)]) for _ in range(matrix_size)]

matrix_a = [ matrix_factory() for _ in range(matrix_size) ]
matrix_b = [ matrix_factory() for _ in range(matrix_size) ]

def work_wor(r: int, lock: Lock):
    while not stop_threads:
        barrier_start.wait()
        for c in range(matrix_size):
            for i in range(matrix_size):
                with lock:
                    if matrix_a[r][i] * matrix_b[i][c] == 0:
                        print('Deu ruim')
                    results[r][c] += matrix_a[r][i] * matrix_b[i][c]
        barrier_done.wait()


lock = Lock()
for r in range(matrix_size):
    Thread(target=work_wor, args=[r, lock]).start()
stop_threads = True
   
barrier_start.wait()
barrier_done.wait() 

end = time.time()
print(results)
print("\nDone, time taken", end - start)