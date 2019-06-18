# Array needs to be sorted
# O(log n)
# o(1)

import random
import math

def binary_search(array, term):

    L = 0
    R = len(array) - 1
    while L <= R:
        M = math.floor( (R + L) / 2)
        if array[M] > term:
            R = M - 1
        if array[M] < term:
            L = M + 1
        if array[M] == term:
            return M
    return -1

arr = sorted(random.sample(range(1, 10), 5))
print("Array: {arr}".format(arr=arr))

target = 3
print("Target: {target}".format(target=target))

idx = binary_search(arr, target)
print("Found: {idx}".format(idx=idx))