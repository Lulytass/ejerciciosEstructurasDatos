import random
import time
import csv


def bubble_sort(arr):
    n = len(arr)
    iteraciones = 0
    for i in range(n):
        for j in range(0, n-i-1):
            iteraciones += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return iteraciones


def selection_sort(arr):
    n = len(arr)
    iteraciones = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            iteraciones += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return iteraciones


def insertion_sort(arr):
    iteraciones = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            iteraciones += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return iteraciones


def merge_sort(arr):
    iteraciones = 0

    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        iteraciones += merge_sort(L)
        iteraciones += merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            iteraciones += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return iteraciones


def shell_sort(arr):
    iteraciones = 0
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                iteraciones += 1
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return iteraciones


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    iteraciones = 0
    if low < high:
        pi = partition(arr, low, high)
        iteraciones += high - low
        iteraciones += quick_sort(arr, low, pi - 1)
        iteraciones += quick_sort(arr, pi + 1, high)
    return iteraciones


def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]


sizes = [10, 100, 1000]  # , 10000, 100000, 1000000

# Abrir archivo CSV para escribir los resultados
with open('sorting_results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Size', 'Method', 'Time (s)', 'Iterations'])

    for size in sizes:
        arr = generate_random_array(size)

        # Bubble Sort
        start_time = time.time()
        iteraciones = bubble_sort(arr.copy())
        end_time = time.time()
        tiempo = end_time - start_time
        writer.writerow([size, 'Bubble Sort', tiempo, iteraciones])

        # Selection Sort
        start_time = time.time()
        iteraciones = selection_sort(arr.copy())
        end_time = time.time()
        tiempo = end_time - start_time
        writer.writerow([size, 'Selection Sort', tiempo, iteraciones])

        # Insertion Sort
        start_time = time.time()
        iteraciones = insertion_sort(arr.copy())
        end_time = time.time()
        tiempo = end_time - start_time
        writer.writerow([size, 'Insertion Sort', tiempo, iteraciones])

        # Merge Sort
        start_time = time.time()
        iteraciones = merge_sort(arr.copy())
        end_time = time.time()
        tiempo = end_time - start_time
        writer.writerow([size, 'Merge Sort', tiempo, iteraciones])

        # Shell Sort
        start_time = time.time()
        iteraciones = shell_sort(arr.copy())
        end_time = time.time()
        tiempo = end_time - start_time
        writer.writerow([size, 'Shell Sort', tiempo, iteraciones])

        # Quick Sort
        start_time = time.time()
        iteraciones = quick_sort(arr.copy(), 0, len(arr) - 1)
        end_time = time.time()
        tiempo = end_time - start_time
        writer.writerow([size, 'Quick Sort', tiempo, iteraciones])
