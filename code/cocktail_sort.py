# O (n2)
# stable
# in place

def cocktail_sort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True

    while swapped == True:
        swapped = False
        for i in range(start, end):            
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if swapped == False:
            break
        
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1
        
my_arr = [4, 9, 2, 7, 3, 1, 5, 6]
print("Initial array : " + str(my_arr))
cocktail_sort(my_arr)
print("Sorted array : " + str(my_arr))

