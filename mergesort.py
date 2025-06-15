import random
import time
import matplotlib.pyplot as plt
from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def measure_execution_time(arr: List[int]) -> float:
    start = time.time()
    merge_sort(arr)
    end = time.time()
    return end - start

def plot_performance():
    input_sizes = [100, 500, 1000, 2000, 5000, 10000]
    times = []

    for size in input_sizes:
        test_data = [random.randint(0, 10000) for _ in range(size)]
        exec_time = measure_execution_time(test_data)
        times.append(exec_time)

    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, times, marker='o', linestyle='-', color='blue')
    plt.title('Merge Sort Performance')
    plt.xlabel('Input Size (number of elements)')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("merge_sort_performance.png")
    plt.show()

if __name__ == "__main__":
    plot_performance()

