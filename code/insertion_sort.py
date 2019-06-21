# O(n 2)
# in place
# stable

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

my_arr = [4, 9, 2, 7, 3, 1, 5, 6]
print("Initial array : " + str(my_arr))
insertion_sort(my_arr)
print("Sorted array : " + str(my_arr))

