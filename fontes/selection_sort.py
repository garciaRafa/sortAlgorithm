import time
import random
import numpy as np
import matplotlib.pyplot as plt

# criar o algoritmo selection-sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# calcular o tempo de execução do algoritmo        
def measure_time(arr):
    start_time = time.time_ns()
    selection_sort(arr)
    end_time = time.time_ns()
    elapsed_time = end_time - start_time
    return elapsed_time

# tamanhos do vetor para testar
n_values = [100, 200, 400, 600, 800]

time_values = []
for n in n_values:
    elapsed_times = []
    for _ in range(100):
        # criar vetor de números aleatórios
        arr = random.sample(range(n), n)

        # medir o tempo de execução
        elapsed_time = measure_time(arr)
        elapsed_times.append(elapsed_time)

    # calcular a média
    average_time = np.mean(elapsed_times)
    time_values.append(average_time)

# plotar o gráfico
plt.style.use('ggplot')
plt.plot(n_values, time_values, 'o-', label='Caso Médio')
plt.xlabel('Tamanho do vetor')
plt.ylabel('Tempo de execução (nanossegundos)')
plt.title('Tempo de execução do Selection Sort')
plt.legend()
plt.show()