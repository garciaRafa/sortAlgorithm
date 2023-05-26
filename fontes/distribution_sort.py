import time
import random
import numpy as np
import matplotlib.pyplot as plt

# criar o algoritmo distribution-sort
def distribution_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, max_value + 1):
        count[i] += count[i - 1]
    output = [0] * len(arr)

    for num in arr:
        output[count[num] - 1] = num
        count[num] -= 1

    return output

# calcular o tempo de execução do algoritmo        
def measure_time(arr):
    start_time = time.time_ns()
    distribution_sort(arr)
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

        # medir o tempo de execução e obter o vetor ordenado
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
plt.title('Tempo de execução do Distribution Sort')
plt.legend()
plt.show()