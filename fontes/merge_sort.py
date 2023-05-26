import time
import random
import numpy as np
import matplotlib.pyplot as plt


# criar o algoritmo merge-sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

# criar o algoritmo merge
def merge(left, right):
    merged = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

# calcular o tempo de execução do algoritmo        
def measure_time(arr):
    start_time = time.time_ns()
    merge_sort(arr)
    end_time = time.time_ns()
    elapsed_time = end_time - start_time
    return elapsed_time

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
plt.plot(n_values, time_values, 'o-', label="Caso Médio")
plt.xlabel('Tamanho do vetor')
plt.ylabel('Tempo de execução (ns)')
plt.title('Tempo de execução Merge Sort')
plt.legend()
plt.show()