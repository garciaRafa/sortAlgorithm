import time
import random
import numpy as np
import matplotlib.pyplot as plt

# criar o algoritmo quick-sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        smaller, equal, greater = partition(arr, pivot)
        return quick_sort(smaller) + equal + quick_sort(greater)

def partition(arr, pivot):
    smaller = []
    equal = []
    greater = []
    for element in arr:
        if element < pivot:
            smaller.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)
    return smaller, equal, greater   

def generate_sorted_array(n):
    return list(range(n))

def generate_random_array(n):
    return random.sample(range(n), n)

# calcular o tempo de execução do algoritmo        
def measure_time(arr):
    start_time = time.time_ns()
    quick_sort(arr)
    end_time = time.time_ns()
    elapsed_time = end_time - start_time
    return elapsed_time

# tamanhos do vetor para testar
n_values = [100, 200, 400, 600, 800]

time_values_sorted = []
time_values_random = []
for n in n_values:
    elapsed_times_sorted = []
    elapsed_times_random = []
    for _ in range(100):
        # pior caso: vetor já ordenado
        vetor_sorted = generate_sorted_array(n)
        elapsed_time_sorted = measure_time(vetor_sorted)
        elapsed_times_sorted.append(elapsed_time_sorted)

        # caso médio: vetor aleatório
        vetor_random = generate_random_array(n)
        elapsed_time_random = measure_time(vetor_random)
        elapsed_times_random.append(elapsed_time_random)
    
    # média de tempo de cada caso
    average_time_sorted = np.mean(elapsed_times_sorted)
    average_time_random = np.mean(elapsed_times_random)
    time_values_sorted.append(average_time_sorted)
    time_values_random.append(average_time_random)
    
# plotar o gráfico
plt.style.use('ggplot')
plt.plot(n_values, time_values_random, 'o-', label='Caso Médio')
plt.plot(n_values, time_values_sorted, 'o-', label='Pior Caso')
plt.xlabel('Tamanho do vetor')
plt.ylabel('Tempo de execução (nanossegundos)')
plt.title('Tempo médio de execução do Quick Sort')
plt.legend()
plt.show()