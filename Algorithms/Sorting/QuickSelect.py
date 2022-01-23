def quickSelect(arr, start, end, k):
    ''' Find the kth smallest data in array arr'''
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

    if j == k - 1: # Smallest value foud
        return arr[j]
    if j > k - 1:
        return quickSelect(arr, start, j-1, k)
    else:
        return quickSelect(arr, j+1, end, k)


arr = [5, 3, 6, 1, 1, 9, 4, 2, 8, 7]
print(quickSelect(list(arr), 0, len(arr)-1, 6))