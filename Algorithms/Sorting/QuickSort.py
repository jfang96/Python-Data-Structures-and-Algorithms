def quickSort(arr, start, end):
    if end - start < 1:
        return arr
    pivotIdx = end # Pivot as last element
    pivotVal = arr[pivotIdx]

    arr[start], arr[pivotIdx] = arr[pivotIdx], arr[start]

    i = start + 1
    j = end

    while j >= i: # While i and j not crossed...
        while j >= i and arr[i] <= pivotVal: # i increments until <= pivotVal
            i += 1
        while j >= i and arr[j] >= pivotVal: # j decrements until >= pivotVal
            j -= 1
        if j >= i: # If i and j not crossed, swap them
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    # Swap start (pivotVal) with j
    arr[start], arr[j] = arr[j], arr[start]

    # Recurse through left and right side of pivot
    quickSort(arr, start, j-1)
    quickSort(arr, j+1, end)
    
    return arr


arr = [5, 3, 6, 1, 9, 4, 2, 8, 7]
print(quickSort(list(arr), 0, len(arr)-1))