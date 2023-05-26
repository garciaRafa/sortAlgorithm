import random
import time
import numpy as np
import matplotlib.pyplot as plt

# criar o algoritmo insertion-sort
def insertion_sort(arr, n):
    # caso base: vetor menor ou igual a 1
    if n <= 1:
        return
    insertion_sort(arr, n - 1)
    end = arr[n - 1]  
    i = n - 2
    while(i>=0 and arr[i] > end):
        arr[i+1] = arr[i]
        i = i - 1
    arr[i + 1] = end


def generate_random_array(n):
    return random.sample(range(n), n)

def generate_sorted_array(n):
    return list(range(n))

def generate_reversed_array(n):
    return list(range(n, 0, -1))

def measure_time(arr):
    start_time = time.time_ns()
    insertion_sort(arr, n)
    end_time = time.time_ns()
    elapsed_time = end_time - start_time
    return elapsed_time

n_values = [100, 200, 400, 600, 800]

time_values_random = []
time_values_sorted = []
time_values_reversed = []
for n in n_values:
    elapsed_times_random = []
    elapsed_times_sorted = []
    elapsed_times_reversed = []
    
    for _ in range(100):
        # caso médio: vetor aleatório
        vetor_random = generate_random_array(n)
        elapsed_time_random = measure_time(vetor_random)
        elapsed_times_random.append(elapsed_time_random)

        # melhor caso: vetor já ordenado
        vetor_sorted = generate_sorted_array(n)
        elapsed_time_sorted = measure_time(vetor_sorted)
        elapsed_times_sorted.append(elapsed_time_sorted)

        # pior caso: vetor ordenado em ordem reversa
        vetor_reversed = generate_reversed_array(n)
        elapsed_time_reversed = measure_time(vetor_reversed)
        elapsed_times_reversed.append(elapsed_time_reversed)
    
    # média de tempo de cada caso
    average_time_random = np.mean(elapsed_times_random)
    average_time_sorted = np.mean(elapsed_times_sorted)
    average_time_reversed = np.mean(elapsed_times_reversed)
    time_values_random.append(average_time_random)
    time_values_sorted.append(average_time_sorted)
    time_values_reversed.append(average_time_reversed)
    
# plotar o gráfico
plt.style.use('ggplot')
plt.plot(n_values, time_values_random, 'o-', label='Caso Médio')
plt.plot(n_values, time_values_sorted, 'o-', label='Melhor Caso')
plt.plot(n_values, time_values_reversed, 'o-', label='Pior Caso')
plt.xlabel('Tamanho do vetor')
plt.ylabel('Tempo de execução (nanossegundos)')
plt.title('Tempo de execução do Insertion Sort')
plt.legend()
plt.show()