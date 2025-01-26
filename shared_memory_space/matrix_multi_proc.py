import multiprocessing
import time
from random import choice, randint
from multiprocessing import Barrier, Process, cpu_count

process_count = cpu_count()
matrix_size = 200

def generate_random_matrix(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row * matrix_size + col] = choice([randint(-100, -1), randint(1, 100)])

def work_out_row(id, matrix_a, matrix_b, result, work_start, work_complete):
    while True:
        work_start.wait()  # Sincronizar todos os processos para começar
        for row in range(id, matrix_size, process_count):  # Distribuir o trabalho entre os processos
            for col in range(matrix_size):
                for i in range(matrix_size):
                    result[row * matrix_size + col] += matrix_a[row * matrix_size + i] * matrix_b[i * matrix_size + col]
        work_complete.wait()  # Sincronizar todos os processos após terminar o trabalho

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    work_start = Barrier(process_count + 1)
    work_complete = Barrier(process_count + 1)
    
    # Arrays compartilhados para armazenar os resultados
    matrix_a = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock=False)
    matrix_b = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock=False)
    result = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock=False)
    
    # Iniciar os processos
    processes = []
    for p in range(process_count):
        p_process = Process(target=work_out_row, args=(p, matrix_a, matrix_b, result, work_start, work_complete))
        processes.append(p_process)
        p_process.start()

    start = time.time()

    # Gerar matrizes e processar o trabalho
    for t in range(10):
        generate_random_matrix(matrix_a)
        generate_random_matrix(matrix_b)
        
        # Resetar o resultado a cada nova iteração
        for i in range(matrix_size * matrix_size):
            result[i] = 0
        
        work_start.wait()  # Espera todos os processos começarem
        work_complete.wait()  # Espera todos os processos terminarem

    # Aguardar o término de todos os processos
    for p_process in processes:
        p_process.terminate()
        p_process.join()

    end = time.time()

    print(*result)
    print("Done, time taken", end - start)