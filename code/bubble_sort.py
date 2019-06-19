# Worst sorting algorithm
# O(n2) - when array reverse sorted
# o(n) - when array already sorted

import random

def bubble_sort(arr):
    swapped = True
    n = len(arr)

    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
    
    return arr

my_arr = random.sample(range(1,100), 10)
print("Initial array : " + str(my_arr))

bubble_sort(my_arr)
print("Sorted array : " + str(my_arr))