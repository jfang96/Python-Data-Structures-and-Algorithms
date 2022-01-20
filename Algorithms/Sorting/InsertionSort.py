def insertionSort(arr):
    for i in range(len(arr)):
        j = i
        while j != 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr


arr = [5, 3, 6, 1, 9, 4, 2, 8, 7]
print(insertionSort(arr))