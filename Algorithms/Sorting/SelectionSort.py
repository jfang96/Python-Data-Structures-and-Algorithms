def selectionSort(arr):
    for i in range(len(arr)):
        minIdx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minIdx]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr


arr = [5, 3, 6, 1, 9, 4, 2, 8, 7]
print(selectionSort(arr))