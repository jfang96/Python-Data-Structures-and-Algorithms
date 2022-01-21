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

def mergeSortPythonic(arr):
    if len(arr) <= 1:
        return arr
    midpoint = len(arr) // 2

    left = mergeSort(arr[:midpoint])
    right = mergeSort(arr[midpoint:])

    # Merge left and right
    newArr = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            newArr.append(left[0])
            del left[0]
        else:
            newArr.append(right[0])
            del right[0]
    
    newArr.extend(left)
    newArr.extend(right)

    return newArr


arr = [5, 3, 6, 1, 9, 4, 2, 8, 7]
print(mergeSort(list(arr)))
print(mergeSortPythonic(list(arr)))
