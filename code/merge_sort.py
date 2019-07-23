# Divide and conquer approach
# time: O(nlog n)
# space: O(n)
# in place
# stable: yes
# usefule for sorting linked list in O(nlogn) time

def merge(arr, left_arr, right_arr):
    i = j = k = 0

    # merge array and sort
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] > right_arr[j]:
            arr[k] = right_arr[j]
            j += 1
        else:
            arr[k] = left_arr[i]
            i += 1
        k += 1

    # leftovers
    while i < len(left_arr):
        arr[k] = left_arr[i]
        k += 1
        i += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        k += 1
        j += 1


def merge_sort(arr):
    if len(arr) < 2:
        return

    l = 0
    r = len(arr)
    m = len(arr) // 2

    left_arr = arr[:m]
    right_arr = arr[m:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    merge(arr, left_arr, right_arr)



my_arr = [4, 2, 7, 3, 1, 5, 6]
print("Initial array : " + str(my_arr))
merge_sort(my_arr)
print("Sorted array : " + str(my_arr))
