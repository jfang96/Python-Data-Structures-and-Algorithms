def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    midpoint = len(arr) // 2
    left = arr[:midpoint]
    right = arr[midpoint:]

    left = mergeSort(left)
    right = mergeSort(right)

    # Merge left and right
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[i+j] = left[i]
            i += 1
        else:
            arr[i+j] = right[j]
            j += 1
    
    while i < len(left):
        arr[i+j] = left[i]
        i += 1
    while j < len(right):
        arr[i+j] = right[j]
        j += 1

    return arr

arr = [5, 3, 6, 1, 9, 4, 2, 8, 7]
print(mergeSort(arr))
