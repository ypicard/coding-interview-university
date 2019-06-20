# worst case : O(n2)
# average case : O(n log n)
# best case : o(n log n)
# not stable
# in place

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


my_arr = [4,2,7,3,1,5,6]
n = len(my_arr) 
print("Initial array : " + str(my_arr))
quick_sort(my_arr, 0, n - 1)
print("Sorted array : " + str(my_arr))
