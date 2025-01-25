import time
from random import randint

def matrix_factory() -> list:
    return [randint(-100, 100) for _ in range(matrix_size)]

matrix_size = 600

matrix_a = [ matrix_factory() for _ in range(matrix_size) ]
matrix_b = [ matrix_factory() for _ in range(matrix_size) ]

start = time.time()
results = [[0] * matrix_size for r in range(matrix_size)]

for r in range(matrix_size):
    for c in range(matrix_size):
        for i in range(matrix_size):
            results[r][c] += matrix_a[r][i] * matrix_b[i][c]

end = time.time()
print(results)
print("\nDone, time taken", end - start)